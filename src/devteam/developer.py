from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from devteam.models import ArchitecureDecision, DeveloperResponse, WorkItem


load_dotenv()


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
)


developer_llm = llm.with_structured_output(
    DeveloperResponse
)


def run_developer(work_item: WorkItem, architecture: ArchitecureDecision) -> DeveloperResponse:

    prompt = f"""
                You are an expert full-stack software developer.

                You are implementing a work item defined by the Lead Architect.

                WORK ITEM

                Title:
                {work_item.title}

                Description:
                {work_item.description}

                Acceptance Criteria:
                {work_item.acceptance_criteria}


                ARCHITECTURE

                Summary:
                {architecture.summary}

                Constraints:
                {architecture.constraints}


                Your responsibilities:

                - Follow the Lead Architect's constraints.
                - Do not redesign the architecture unless absolutely necessary.
                - Produce a concise implementation plan.
                - Produce appropriate implementation/code.
                - Clearly state assumptions.
                - Ensure the implementation satisfies the acceptance criteria.
                """
    return developer_llm.invoke(prompt)