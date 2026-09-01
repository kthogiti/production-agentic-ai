from devteam.developer import run_developer
from devteam.developers import get_developer
from devteam.state import DevelopmentState


def developer_node(state: DevelopmentState) -> DevelopmentState:
    lead_response = state["lead_response"]
    work_item = state["current_work_item"]
    developer = get_developer(state["current_developer_id"])

    feedback = None
    review = state.get("review_response")
    if review and not review.approved:
        feedback = review.feedback

    response = run_developer(
        work_item,
        lead_response.architecture,
        developer,
        feedback,
    )

    return {"developer_response": response}
