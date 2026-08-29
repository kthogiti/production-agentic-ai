from typing import TypedDict

from devteam.models import DeveloperResponse, LeadResponse


class DevelopmentState(TypedDict, total=False):
    requirement: str
    lead_response: LeadResponse
    developer_response: DeveloperResponse