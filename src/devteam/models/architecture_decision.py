from pydantic import BaseModel, Field


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
