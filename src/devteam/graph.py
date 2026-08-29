from langgraph.graph import StateGraph, START, END

from devteam.developer import run_developer
from devteam.lead import run_lead
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
    response = run_developer(
        lead_response.work_item, lead_response.architecture
    )

    return {
        "developer_response": response
    }



builder = StateGraph(DevelopmentState)


builder.add_node("lead", lead_node)

builder.add_node("developer",developer_node)

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
    END,
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