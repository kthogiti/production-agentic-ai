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
