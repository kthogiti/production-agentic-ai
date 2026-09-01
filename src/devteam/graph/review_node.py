from devteam.lead import review_implementation
from devteam.state import DevelopmentState


def review_node(state: DevelopmentState) -> DevelopmentState:
    review = review_implementation(
        lead_response=state["lead_response"],
        work_item=state["current_work_item"],
        developer_response=state["developer_response"],
    )

    attempts = state.get("review_attempts", 0) + 1

    return {
        "review_response": review,
        "review_attempts": attempts,
    }
