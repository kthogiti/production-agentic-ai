from devteam.graph import graph


if __name__ == "__main__":
    result = graph.invoke(
        {
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
