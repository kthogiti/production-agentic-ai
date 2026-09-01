from devteam.state import DevelopmentState


def complete_work_item_node(state: DevelopmentState) -> DevelopmentState:
    completed = list(state.get("completed_work_items", []))
    current = state["current_work_item"]

    completed.append(current.id)
    next_index = state["current_work_item_index"] + 1

    return {
        "completed_work_items": completed,
        "current_work_item_index": next_index,
    }
