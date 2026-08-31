from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from devteam.models import DeveloperResponse, LeadResponse, ReviewResponse


load_dotenv()


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
)


lead_llm = llm.with_structured_output(
    LeadResponse
)


def run_lead(requirement: str) -> LeadResponse:

    prompt = f"""
                You are the Lead Software Architect of an AI software
                development team.

                Your responsibilities are:

                - Understand the software requirement.
                - Define an appropriate high-level architecture.
                - Avoid unnecessary complexity.
                - Define technical constraints for developers.
                - Create one clear implementation work item.
                - Define measurable acceptance criteria.
                - Do not write the full implementation.
                - Do not invent business requirements.

                Software requirement:

                {requirement}
                """
    return lead_llm.invoke(prompt)

review_llm = llm.with_structured_output(
    ReviewResponse
)


def review_implementation(lead_response: LeadResponse,
    developer_response: DeveloperResponse
    ) -> ReviewResponse:

    prompt = f"""
                You are the Lead Software Architect reviewing a developer's work.

                Your job is to verify whether the implementation:

                - follows the architecture
                - respects technical constraints
                - satisfies acceptance criteria
                - avoids unnecessary design changes
                - avoids inventing requirements
                - is maintainable and reasonable

                ARCHITECTURE

                {lead_response.architecture}

                WORK ITEM

                {lead_response.work_item}

                DEVELOPER RESPONSE

                Understanding:
                {developer_response.understanding}

                Plan:
                {developer_response.plan}

                Implementation:
                {developer_response.implementation}

                Assumptions:
                {developer_response.assumptions}

                If the implementation is acceptable, approve it.

                If changes are required:
                - reject it
                - provide concise and actionable feedback
                - do not rewrite the entire implementation yourself
                """

    return review_llm.invoke(prompt)