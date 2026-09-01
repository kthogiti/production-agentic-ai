from pydantic import BaseModel, Field


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
