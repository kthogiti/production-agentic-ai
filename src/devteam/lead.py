from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from devteam.models import LeadResponse


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