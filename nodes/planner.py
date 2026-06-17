from config import *
from langchain_google_vertexai import ChatVertexAI


llm = ChatVertexAI(
    model="gemini-2.5-flash"
)


def planner_node(state):

    response = llm.invoke(
        f"""
        You are an investment research planner.

        Create a detailed research plan.

        Question:

        {state["question"]}

        Include:

        - Business Model
        - Revenue Streams
        - Competition
        - Risks
        - Recommendation
        """
    )

    return {
        "research_plan": response.content
    }