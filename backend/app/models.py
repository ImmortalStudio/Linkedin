from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, UUID4

class Campaign(BaseModel):
    id: Optional[UUID4] = None
    name: str
    description: Optional[str] = None
    active: bool
    search_criteria: Optional[dict] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class CompanyProfile(BaseModel):
    id: Optional[UUID4] = None
    company_name: str
    mission_statement: Optional[str] = None
    vision_statement: Optional[str] = None
    value_proposition: Optional[str] = None
    key_differentiators: Optional[List[str]] = None
    unique_features: Optional[List[str]] = None
    primary_industry: str
    secondary_industries: Optional[List[str]] = None
    target_company_size: Optional[List[str]] = None
    target_regions: Optional[str] = None
    target_job_titles: Optional[str] = None
    customer_pain_points: Optional[List[str]] = None
    solution_benefits: Optional[List[str]] = None
    is_active: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    last_reviewed_at: Optional[datetime] = None

class Lead(BaseModel):
    id: Optional[UUID4] = None
    full_name: Optional[str] = None
    linkedin_url: Optional[str] = None
    title: Optional[str] = None
    company_name: Optional[str] = None
    location: Optional[str] = None
    status: str
    campaign_id: Optional[UUID4] = None
    company_profile_id: Optional[UUID4] = None
    last_contacted_at: Optional[datetime] = None
    next_followup_due_at: Optional[datetime] = None
    notes: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class Meeting(BaseModel):
    id: Optional[UUID4] = None
    lead_id: UUID4
    scheduled_time: Optional[datetime] = None
    calendly_link: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class Message(BaseModel):
    id: Optional[UUID4] = None
    lead_id: UUID4
    template_id: Optional[UUID4] = None
    topic: str
    extension: str
    message_type: str
    payload: Optional[dict] = None
    content: str
    event: Optional[str] = None
    sent_at: Optional[datetime] = None
    response_received: Optional[bool] = None
    private: Optional[bool] = None
    response_content: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    inserted_at: datetime

class TaskExecutionLog(BaseModel):
    id: Optional[UUID4] = None
    task_id: UUID4
    task_name: str
    executed_at: datetime
    status: str
    error_message: Optional[str] = None
    execution_details: Optional[dict] = None

class TaskLibrary(BaseModel):
    id: Optional[UUID4] = None
    name: str
    description: Optional[str] = None
    task_type: str
    config: dict
    is_active: Optional[bool] = None
    target: int
    completed: int
    status: str
    last_completed_at: Optional[datetime] = None
    schedule_config: Optional[dict] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class Template(BaseModel):
    id: Optional[UUID4] = None
    name: str
    template_type: str
    content: str
    active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
