from devteam.models import DeveloperResponse, LeadResponse, ReviewResponse, WorkItem
from devteam.models.architecture_decision import ArchitecureDecision
from devteam.models.developer_response import DeveloperResponse as DirectDeveloperResponse
from devteam.models.lead_response import LeadResponse as DirectLeadResponse
from devteam.models.review_response import ReviewResponse as DirectReviewResponse
from devteam.models.work_item import WorkItem as DirectWorkItem


def test_models_are_available_from_package_and_modules() -> None:
    assert DeveloperResponse is DirectDeveloperResponse
    assert LeadResponse is DirectLeadResponse
    assert ReviewResponse is DirectReviewResponse
    assert WorkItem is DirectWorkItem
    assert ArchitecureDecision.__name__ == "ArchitecureDecision"
