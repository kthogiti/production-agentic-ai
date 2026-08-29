from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from devteam.models import DeveloperResponse


load_dotenv()


llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
)


developer_llm = llm.with_structured_output(
    DeveloperResponse
)


def run_developer(task: str) -> DeveloperResponse:

    prompt = f"""
                You are an expert full-stack software developer.

                You are part of an AI software development team.

                Your responsibilities are:

                - Understand the assigned task.
                - Think about maintainability and clean architecture.
                - Produce a short implementation plan.
                - Produce appropriate implementation/code.
                - Clearly state assumptions.
                - Do not invent requirements that were not provided.

                Assigned task:

                {task}
                """
    return developer_llm.invoke(prompt)