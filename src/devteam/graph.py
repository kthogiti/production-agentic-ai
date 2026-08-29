from langgraph.graph import StateGraph, START, END

from devteam.developer import run_developer
from devteam.state import DevelopmentState


def developer_node(state: DevelopmentState) -> DevelopmentState:
    response = run_developer(
        state["task"]
    )

    return {
        "developer_response": response
    }


builder = StateGraph(
    DevelopmentState
)

builder.add_node(
    "developer",
    developer_node,
)

builder.add_edge(
    START,
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
        "task": """
                We have an ASP.NET Core Web API.

                Create an endpoint:

                POST /api/customers

                The request contains name and email.

                Return HTTP 201 after creating the customer.
                """
        }
    )

    response = result[
        "developer_response"
    ]

    # print("\nGiven Task:")
    # print(response.taskStatement)

    print("\nUNDERSTANDING")
    print(response.understanding)

    print("\nPLAN")

    for step in response.plan:
        print(f"- {step}")

    print("\nIMPLEMENTATION")
    print(response.implementation)

    print("\nASSUMPTIONS")

    for assumption in response.assumptions:
        print(f"- {assumption}")