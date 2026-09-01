from devteam.state import DevelopmentState
from devteam.lead import run_lead


def lead_node(state: DevelopmentState) -> DevelopmentState:
    response = run_lead(state["requirement"])

    return {
        "lead_response": response,
        "current_work_item_index": 0,
        "completed_work_items": [],
    }
