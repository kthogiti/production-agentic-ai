from langgraph.graph import END, START, StateGraph

from devteam.state import DevelopmentState

from .assign_developer_node import assign_developer_node
from .complete_work_item_node import complete_work_item_node
from .developer_node import developer_node
from .lead_node import lead_node
from .review_node import review_node
from .select_work_item_node import select_work_item_node


def route_after_review(state: DevelopmentState) -> str:
    review = state["review_response"]

    if review.approved:
        return "complete"

    if state.get("review_attempts", 0) >= 2:
        return "complete"

    return "revise"


def route_after_completion(state: DevelopmentState) -> str:
    next_index = state["current_work_item_index"]
    work_items = state["lead_response"].work_items

    if next_index >= len(work_items):
        return "done"

    return "next"


builder = StateGraph(DevelopmentState)

builder.add_node("lead", lead_node)
builder.add_node("select_work_item", select_work_item_node)
builder.add_node("developer", developer_node)
builder.add_node("assign_developer", assign_developer_node)
builder.add_node("review", review_node)
builder.add_node("complete_work_item", complete_work_item_node)

builder.add_edge(START, "lead")
builder.add_edge("lead", "select_work_item")
builder.add_edge("select_work_item", "assign_developer")
builder.add_edge("assign_developer", "developer")
builder.add_edge("developer", "review")

builder.add_conditional_edges(
    "review",
    route_after_review,
    {
        "complete": "complete_work_item",
        "revise": "developer",
    },
)

builder.add_conditional_edges(
    "complete_work_item",
    route_after_completion,
    {
        "next": "select_work_item",
        "done": END,
    },
)

graph = builder.compile()

__all__ = [
    "graph",
    "assign_developer_node",
    "lead_node",
    "developer_node",
    "review_node",
    "complete_work_item_node",
    "select_work_item_node",
    "route_after_review",
    "route_after_completion",
    "builder",
]


if __name__ == "__main__":
    result = graph.invoke(
        {
            # "requirement": """
            #     Build an ASP.NET Core Web API endpoint:

            #     POST /api/customers

            #     The request contains:
            #     - name
            #     - email

            #     The endpoint should create a customer and return HTTP 201.
            #     """
            "requirement": """
                Build customer management functionality for an
                ASP.NET Core Web API.

                Requirements:

                - Customer has Id, Name and Email.
                - Create customers.
                - Retrieve customer by Id.
                - Validate name and email.
                - Return appropriate HTTP responses.
                - Add unit tests for customer creation.
            """
        }
    )

    lead = result["lead_response"]

    print("\n=== IMPLEMENTATION PLAN ===")

    for item in lead.work_items:
        print(f"\n{item.id}: {item.title}")
        print(item.description)
        for criterion in item.acceptance_criteria:
            print(f"- {criterion}")

        developer = result["developer_response"]
        print("\n=== DEVELOPER ===")
        print(f"{item.id} assigned to developer: {developer.assigned_developer_id}")
        print(developer.understanding)
        print(developer.plan)
        print(developer.implementation)
        print(developer.assumptions)

        review = result["review_response"]
        print("\n=== REVIEW ===")
        print(f"Approved: {review.approved}")
        print(review.summary)

        for item in review.feedback:
            print(f"- {item}")

        print(f"\nReview attempts: {result.get('review_attempts', 0)}")