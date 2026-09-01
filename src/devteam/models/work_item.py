from pydantic import BaseModel, Field


class WorkItem(BaseModel):
    id: str = Field(
        description="Unique work item identifier such as WI-001."
    )
    title: str
    description: str
    acceptance_criteria: list[str]
