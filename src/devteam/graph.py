from langgraph.graph import StateGraph, START, END

from devteam.developer import run_developer
from devteam.lead import review_implementation, run_lead
from devteam.state import DevelopmentState



def lead_node(state: DevelopmentState) -> DevelopmentState:
    response = run_lead(
        state["requirement"]
    )

    return {
        "lead_response": response,
        "current_work_item_index": 0,
        "completed_work_items": []
    }

def developer_node(state: DevelopmentState) -> DevelopmentState:
    lead_response = state["lead_response"]

    work_item = state["current_work_item"]

    feedback = None
    if "review_response" in state:
        if not state["review_response"].approved:
            feedback = state["review_response"].feedback

    response = run_developer(
        work_item, lead_response.architecture, feedback
    )

    return {
        "developer_response": response
    }

def review_node(state: DevelopmentState) -> DevelopmentState:

    review = review_implementation(
        lead_response=state["lead_response"],
        work_item=state["current_work_item"],
        developer_response=state["developer_response"],
    )

    attempts = state.get("review_attempts",0) + 1

    return {
        "review_response": review,
        "review_attempts": attempts
    }

def complete_work_item_node(state: DevelopmentState) -> DevelopmentState:

    completed = list(
        state.get("completed_work_items", [])
    )

    current = state[
        "current_work_item"
    ]

    completed.append(
        current.id
    )

    next_index = (
        state[
            "current_work_item_index"
        ] + 1
    )

    return {
        "completed_work_items": completed,
        "current_work_item_index": next_index,
    }

def route_after_review(state: DevelopmentState) -> str:

    review = state["review_response"]

    if review.approved:
        return "complete"

    if state.get("review_attempts", 0) >= 2:
        return "complete"

    return "revise"

def route_after_completion(state: DevelopmentState) -> str:

    next_index = state[
        "current_work_item_index"
    ]

    work_items = state[
        "lead_response"
    ].work_items

    if next_index >= len(work_items):
        return "done"

    return "next"

def select_work_item_node(state: DevelopmentState) -> DevelopmentState:
    index = state.get("current_work_item_index", 0)
    lead_response = state["lead_response"]
    work_items = lead_response.work_items

    work_item = work_items[index]

    return {
        "current_work_item": work_item,
        "review_attempts": 0
    }

builder = StateGraph(DevelopmentState)


builder.add_node("lead", lead_node)

builder.add_node("select_work_item",select_work_item_node)
builder.add_node("developer",developer_node)
builder.add_node("review", review_node)
builder.add_node("complete_work_item",complete_work_item_node)

builder.add_edge(
    START,
    "lead",
)

builder.add_edge(
    "lead",
    "select_work_item",
)

builder.add_edge(
    "select_work_item",
    "developer",
)

builder.add_edge(
    "developer",
    "review",
)

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

if __name__ == "__main__":

    result = graph.invoke(
        # {
        #     "task": """
        #             Create a C# record named Customer with:

        #             - Guid Id
        #             - string Name
        #             - string Email

        #             Use modern C# syntax.
        #             """
        # }
        {
        "requirement": """
                Build an ASP.NET Core Web API endpoint:

                POST /api/customers

                The request contains:
                - name
                - email

                The endpoint should create a customer and return HTTP 201.
                """
        }
    )

    lead = result["lead_response"]

    print("\n=== IMPLEMENTATION PLAN ===")

    for item in lead.work_items:

        print(
            f"\n{item.id}: "
            f"{item.title}"
        )

        print(
            item.description
        )

        for criterion in (item.acceptance_criteria):
            print(
                f"- {criterion}"
            )

        developer = result["developer_response"]
        print("\n=== DEVELOPER ===")
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

        print(
            f"\nReview attempts: "
            f"{result.get('review_attempts', 0)}"
        )