from langgraph.graph import StateGraph, START, END

from devteam.developer import run_developer
from devteam.lead import review_implementation, run_lead
from devteam.state import DevelopmentState



def lead_node(state: DevelopmentState) -> DevelopmentState:
    response = run_lead(
        state["requirement"]
    )

    return {
        "lead_response": response
    }

def developer_node(state: DevelopmentState) -> DevelopmentState:
    lead_response = state.get("lead_response")

    feedback = None
    if "review_response" in state:
        if not state["review_response"].approved:
            feedback = state["review_response"].feedback

    response = run_developer(
        lead_response.work_item, lead_response.architecture, feedback
    )

    return {
        "developer_response": response
    }

def review_node(state: DevelopmentState) -> DevelopmentState:

    review = review_implementation(
        lead_response=state["lead_response"],
        developer_response=state["developer_response"],
    )

    attempts = state.get("review_attempts",0) + 1

    return {
        "review_response": review,
        "review_attempts": attempts,
    }

def route_after_review(state: DevelopmentState) -> str:

    review = state["review_response"]

    if review.approved:
        return "approved"

    if state.get("review_attempts", 0) >= 2:
        return "approved"

    return "revise"

builder = StateGraph(DevelopmentState)


builder.add_node("lead", lead_node)
builder.add_node("developer",developer_node)
builder.add_node("review", review_node)

builder.add_edge(
    START,
    "lead",
)

builder.add_edge(
    "lead",
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
        "approved": END,
        "revise": "developer",
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
    developer = result["developer_response"]

    print("\n=== LEAD ===")
    print(lead.requirement_understanding)
    print(lead.architecture)
    print(lead.work_item)

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