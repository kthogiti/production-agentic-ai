from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from devteam.models import ArchitecureDecision, DeveloperResponse, WorkItem
from devteam.models.developer_profile import DeveloperProfile


load_dotenv()


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
)


developer_llm = llm.with_structured_output(
    DeveloperResponse
)


def run_developer(work_item: WorkItem, 
                  architecture: ArchitecureDecision,
                  developer: DeveloperProfile, 
                  feedback: list[str] | None = None) -> DeveloperResponse:

    feedback_section = ""

    if feedback:
        feedback_section = f"""
        REVIEW FEEDBACK

        {feedback}

        You must address this feedback in the revised implementation.
        """

    prompt = f"""
                You are {developer.name}.

                You are an expert full-stack software developer
                working as part of an AI software development team.

                Your skills include:

                {developer.skills}

                WORK ITEM

                ID:
                {work_item.id}

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

                {feedback_section}

                Your responsibilities:

                - Implement only the assigned work item.
                - Follow the Lead's architecture.
                - Respect all constraints.
                - Satisfy acceptance criteria.
                - Address review feedback if supplied.
                - Avoid unrelated changes.
                - Clearly state assumptions.
                """
    return developer_llm.invoke(prompt)