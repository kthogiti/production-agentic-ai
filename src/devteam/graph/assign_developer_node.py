from devteam.developers import DEVELOPERS
from devteam.state import DevelopmentState


def assign_developer_node(
    state: DevelopmentState,
) -> DevelopmentState:

    index = state["current_work_item_index"]

    developer = DEVELOPERS[index % len(DEVELOPERS)]
    
    print(
        f"Assigned to "
        f"{developer.id}"
    )

    return {
        "current_developer_id": developer.id
    }