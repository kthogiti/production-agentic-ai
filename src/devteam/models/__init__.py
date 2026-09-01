from pydantic import BaseModel, Field


class DeveloperResponse(BaseModel):
    # taskStatement: str = Field(
    #     description="The original task statement provided to the developer detailed into minimum 50 words."
    # )
    understanding: str = Field(
        description="Developer's understanding of the assigned task."
    )

    plan: list[str] = Field(
        description="Steps the developer proposes to complete the task."
    )

    implementation: str = Field(
        description="Proposed implementation or code."
    )

    assumptions: list[str] = Field(
        default_factory=list,
        description="Any assumptions made by the developer."
    )

class ArchitecureDecision(BaseModel):
    summary: str = Field(
        description="high-level architecture approach."
    )
    constraints: list[str] = Field(
        description="Technical constraints that developer must follow."
    )
    assumptions: list[str] = Field(
        default_factory=list
    )

class ReviewResponse(BaseModel):
    approved: bool = Field(
        description="Whether the implementation is approved."
    )

    feedback: list[str] = Field(
        default_factory=list,
        description="Specific changes required if not approved."
    )

    summary: str = Field(
        description="Short review summary."
    )

class WorkItem(BaseModel):
    id: str = Field(
        description="Unique work item identifier such as WI-001."
    )
    title: str
    description: str
    acceptance_criteria: list[str]

class LeadResponse(BaseModel):
    requirement_understanding: str
    architecture: ArchitecureDecision
    work_items: list[WorkItem] = Field(
        description="Ordered implementation work items required to deliver the requirement."
    )