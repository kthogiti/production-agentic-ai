from typing import TypedDict

from devteam.models import DeveloperResponse


class DevelopmentState(TypedDict, total=False):
    task: str
    developer_response: DeveloperResponse