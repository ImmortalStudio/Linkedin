from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from datetime import datetime

from ..database import get_supabase
from ..models import Campaign, Lead, Message, Meeting, TaskLibrary
from ..agents.bdr_agent import BDRAgent
from ..services.scheduler import TaskScheduler

router = APIRouter()
bdr_agent = None
task_scheduler = TaskScheduler()

@router.on_event("startup")
async def startup_event():
    """Initialize BDR agent and task scheduler on startup"""
    global bdr_agent
    from ..ae.core.system_orchestrator import SystemOrchestrator
    
    orchestrator = SystemOrchestrator()
    bdr_agent = BDRAgent(orchestrator)
    await bdr_agent.initialize_automation()
    await task_scheduler.initialize()

@router.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    task_scheduler.shutdown()

@router.post("/campaigns/", response_model=Campaign)
async def create_campaign(campaign: Campaign):
    """Create a new outreach campaign"""
    async for supabase in get_supabase():
        result = await supabase.table("campaigns").insert(campaign.dict()).execute()
        return Campaign(**result.data[0])

@router.get("/campaigns/", response_model=List[Campaign])
async def list_campaigns():
    """List all campaigns"""
    async for supabase in get_supabase():
        result = await supabase.table("campaigns").select("*").execute()
        return [Campaign(**item) for item in result.data]

@router.post("/campaigns/{campaign_id}/start")
async def start_campaign(campaign_id: UUID4):
    """Start an outreach campaign"""
    await bdr_agent.execute_outreach_campaign(str(campaign_id))
    return {"status": "started", "campaign_id": campaign_id}

@router.post("/leads/", response_model=Lead)
async def create_lead(lead: Lead):
    """Create a new lead"""
    async for supabase in get_supabase():
        result = await supabase.table("leads").insert(lead.dict()).execute()
        return Lead(**result.data[0])

@router.get("/leads/", response_model=List[Lead])
async def list_leads(campaign_id: Optional[UUID4] = None):
    """List leads, optionally filtered by campaign"""
    async for supabase in get_supabase():
        query = supabase.table("leads").select("*")
        if campaign_id:
            query = query.eq("campaign_id", str(campaign_id))
        result = await query.execute()
        return [Lead(**item) for item in result.data]

@router.post("/leads/{lead_id}/schedule-call")
async def schedule_call(lead_id: UUID4, calendly_link: str):
    """Schedule a call with a lead"""
    async for supabase in get_supabase():
        lead = await supabase.table("leads").select("*").eq("id", str(lead_id)).single()
        await bdr_agent.schedule_call(lead.data, calendly_link)
        return {"status": "scheduled", "lead_id": lead_id}

@router.post("/tasks/", response_model=TaskLibrary)
async def create_task(task: TaskLibrary):
    """Create a new scheduled task"""
    async for supabase in get_supabase():
        result = await supabase.table("task_library").insert(task.dict()).execute()
        created_task = TaskLibrary(**result.data[0])
        if created_task.is_active and created_task.schedule_config:
            task_scheduler.schedule_task(created_task.dict())
        return created_task

@router.get("/tasks/", response_model=List[TaskLibrary])
async def list_tasks():
    """List all tasks"""
    async for supabase in get_supabase():
        result = await supabase.table("task_library").select("*").execute()
        return [TaskLibrary(**item) for item in result.data]

@router.post("/messages/{lead_id}/handle-response")
async def handle_lead_response(lead_id: UUID4, response_content: str):
    """Handle a response from a lead"""
    await bdr_agent.handle_response(str(lead_id), response_content)
    return {"status": "processed", "lead_id": lead_id}
