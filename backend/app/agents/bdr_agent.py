import os
from typing import Dict, Any, Optional
from datetime import datetime
from ..database import get_supabase
from ..ae.core import (
    AutogenWrapper,
    SystemOrchestrator,
    click_using_selector,
    enter_text_and_click,
    open_url
)

class BDRAgent:
    def __init__(self, orchestrator=None):
        """Initialize BDR Agent with optional orchestrator instance.
        
        Args:
            orchestrator: Pre-configured orchestrator instance for LinkedIn automation
        """
        self.orchestrator = orchestrator
        self.autogen = AutogenWrapper()
        self.supabase = get_supabase()
        
    async def initialize_automation(self):
        """Initialize the automation system with required configurations"""
        if not self.orchestrator:
            self.orchestrator = SystemOrchestrator()
            await self.orchestrator.initialize()
            
        # Configure AutoGen with environment variables
        config = {
            "model_name": os.getenv("AUTOGEN_MODEL_NAME"),
            "api_key": os.getenv("AUTOGEN_MODEL_API_KEY"),
            "base_url": os.getenv("AUTOGEN_MODEL_BASE_URL"),
            "api_type": os.getenv("AUTOGEN_MODEL_API_TYPE"),
            "api_version": os.getenv("AUTOGEN_MODEL_API_VERSION"),
        }
        self.autogen.configure(config)
        
    async def execute_outreach_campaign(self, campaign_id: str):
        """Execute an outreach campaign for leads"""
        async for supabase in get_supabase():
            # Get campaign details
            campaign = await supabase.table("campaigns").select("*").eq("id", campaign_id).single()
            
            # Get leads for campaign
            leads = await supabase.table("leads").select("*").eq("campaign_id", campaign_id).execute()
            
            for lead in leads.data:
                await self.process_lead(lead)
                
    async def process_lead(self, lead: Dict[str, Any]):
        """Process a single lead with automated outreach"""
        # Navigate to lead's LinkedIn profile
        await self.orchestrator.execute_skill(
            open_url,
            {"url": lead["linkedin_url"]}
        )
        
        # Perform connection request if not connected
        await self.check_and_connect(lead)
        
        # Send follow-up message if connected
        await self.send_follow_up_message(lead)
        
    async def check_and_connect(self, lead: Dict[str, Any]) -> bool:
        """Check connection status and send connection request if needed.
        
        Args:
            lead: Dictionary containing lead information
            
        Returns:
            bool: True if connected (either previously or now), False otherwise
        """
        if not self.orchestrator:
            raise ValueError("Orchestrator not initialized")
            
        # Visit profile
        await self.orchestrator.execute_skill(
            open_url,
            {"url": lead["linkedin_url"]}
        )
        
        # Check if connect button exists
        connect_exists = await self.orchestrator.execute_skill(
            click_using_selector,
            {"selector": "button[aria-label*='Connect']", "check_only": True}
        )
        
        if connect_exists:
            # Send connection request
            await self.orchestrator.execute_skill(
                click_using_selector,
                {"selector": "button[aria-label*='Connect']"}
            )
            
            # Click send in the modal
            await self.orchestrator.execute_skill(
                click_using_selector,
                {"selector": "button[aria-label*='Send now']"}
            )
            return False
        
        return True
        
    async def send_follow_up_message(self, lead: Dict[str, Any]):
        """Send a follow-up message to a connected lead.
        
        Args:
            lead: Dictionary containing lead information
        """
        if not self.orchestrator:
            raise ValueError("Orchestrator not initialized")
            
        # Click message button
        await self.orchestrator.execute_skill(
            click_using_selector,
            {"selector": "button[aria-label*='Message']"}
        )
        
        # Get message template
        async for supabase in get_supabase():
            campaign = await supabase.table("campaigns").select("*").eq("id", lead["campaign_id"]).single()
            message_template = campaign.data["message_template"]
            
            # Format message with lead data
            message = message_template.format(
                name=lead["name"],
                company=lead.get("company", "your company"),
                title=lead.get("title", "professional")
            )
            
            # Type and send message
            await self.orchestrator.execute_skill(
                enter_text_and_click,
                {
                    "text": message,
                    "input_selector": "div[role='textbox']",
                    "button_selector": "button[aria-label*='Send']"
                }
            )
            
            # Update lead status
            await supabase.table("leads").update({
                "status": "messaged",
                "last_contacted": datetime.utcnow().isoformat()
            }).eq("id", lead["id"]).execute()
        
    async def schedule_call(self, lead: Dict[str, Any], calendly_link: str):
        """Schedule a call using Calendly integration"""
        # Update lead status
        async for supabase in get_supabase():
            await supabase.table("meetings").insert({
                "lead_id": lead["id"],
                "calendly_link": calendly_link,
                "status": "pending",
                "created_at": datetime.utcnow().isoformat()
            }).execute()
            
            # Update lead status
            await supabase.table("leads").update({
                "status": "meeting_scheduled",
                "updated_at": datetime.utcnow().isoformat()
            }).eq("id", lead["id"]).execute()
            
    async def handle_response(self, lead_id: str, response_content: str):
        """Handle responses from leads"""
        async for supabase in get_supabase():
            # Log the response
            await supabase.table("messages").update({
                "response_received": True,
                "response_content": response_content,
                "updated_at": datetime.utcnow().isoformat()
            }).eq("lead_id", lead_id).execute()
