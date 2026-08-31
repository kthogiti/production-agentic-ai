from typing import TypedDict

from devteam.models import DeveloperResponse, LeadResponse, ReviewResponse


class DevelopmentState(TypedDict, total=False):
    requirement: str
    lead_response: LeadResponse
    developer_response: DeveloperResponse
    review_response: ReviewResponse
    review_attempts: int #Stop from creating an infinite loop