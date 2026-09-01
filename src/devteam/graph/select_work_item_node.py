from devteam.state import DevelopmentState


def select_work_item_node(state: DevelopmentState) -> DevelopmentState:
    index = state.get("current_work_item_index", 0)
    lead_response = state["lead_response"]
    work_items = lead_response.work_items

    work_item = work_items[index]

    print(
        f"\nExecuting "
        f"{work_item.id}"
    )

    return {
        "current_work_item": work_item,
        "review_attempts": 0,
    }
