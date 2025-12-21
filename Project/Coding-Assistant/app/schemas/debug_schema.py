from pydantic import BaseModel, Field
from typing import Optional

class DebugResult(BaseModel):
    error_type: str
    root_cause: str
    suggested_fix: str

    jira_ticket_required: bool = Field(
        description="Whether a Jira ticket should be created"
    )

    jira_ticket_id: Optional[str] = None


