from pydantic import BaseModel, Field

from .architecture_decision import ArchitecureDecision
from .work_item import WorkItem


class LeadResponse(BaseModel):
    requirement_understanding: str
    architecture: ArchitecureDecision
    work_items: list[WorkItem] = Field(
        description="Ordered implementation work items required to deliver the requirement."
    )
