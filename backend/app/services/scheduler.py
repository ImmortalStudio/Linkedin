from datetime import datetime
from typing import Dict, Any
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from ..database import get_supabase
from ..agents.bdr_agent import BDRAgent

class TaskScheduler:
    def __init__(self):
        self.scheduler = AsyncIOScheduler()
        self.bdr_agent = BDRAgent()
        
    async def initialize(self):
        """Initialize the scheduler and load tasks"""
        await self.bdr_agent.initialize_automation()
        await self.load_scheduled_tasks()
        self.scheduler.start()
        
    async def load_scheduled_tasks(self):
        """Load scheduled tasks from the database"""
        async for supabase in get_supabase():
            tasks = await supabase.table("task_library").select("*").eq("is_active", True).execute()
            
            for task in tasks.data:
                if task["schedule_config"]:
                    self.schedule_task(task)
                    
    def schedule_task(self, task: Dict[str, Any]):
        """Schedule a task based on its configuration"""
        schedule_config = task["schedule_config"]
        
        if not schedule_config:
            return
            
        trigger = CronTrigger(**schedule_config)
        
        self.scheduler.add_job(
            self.execute_task,
            trigger=trigger,
            args=[task],
            id=str(task["id"]),
            replace_existing=True
        )
        
    async def execute_task(self, task: Dict[str, Any]):
        """Execute a scheduled task"""
        async for supabase in get_supabase():
            # Log task execution start
            log_entry = {
                "task_id": task["id"],
                "task_name": task["name"],
                "executed_at": datetime.utcnow().isoformat(),
                "status": "running"
            }
            
            log_result = await supabase.table("task_execution_logs").insert(log_entry).execute()
            log_id = log_result.data[0]["id"]
            
            try:
                if task["task_type"] == "outreach_campaign":
                    await self.bdr_agent.execute_outreach_campaign(task["config"]["campaign_id"])
                    status = "completed"
                    error_message = None
                else:
                    status = "failed"
                    error_message = f"Unknown task type: {task['task_type']}"
                    
            except Exception as e:
                status = "failed"
                error_message = str(e)
                
            # Update task execution log
            await supabase.table("task_execution_logs").update({
                "status": status,
                "error_message": error_message,
                "execution_details": {"completed_at": datetime.utcnow().isoformat()}
            }).eq("id", log_id).execute()
            
            # Update task completion count
            if status == "completed":
                await supabase.table("task_library").update({
                    "completed": task["completed"] + 1,
                    "last_completed_at": datetime.utcnow().isoformat()
                }).eq("id", task["id"]).execute()
                
    def shutdown(self):
        """Shutdown the scheduler"""
        self.scheduler.shutdown()
