from typing import TypedDict

from devteam.models import DeveloperResponse, LeadResponse, ReviewResponse, WorkItem


class DevelopmentState(TypedDict, total=False):
    requirement: str

    lead_response: LeadResponse

    current_work_item_index: int
    current_work_item: WorkItem

    current_developer_id: str
    
    developer_response: DeveloperResponse
    review_response: ReviewResponse
    
    review_attempts: int #Stop from creating an infinite loop

    completed_work_items: list[str]