from config import *
from langchain_google_vertexai import ChatVertexAI


llm = ChatVertexAI(
    model="gemini-2.5-flash"
)


def research_node(state):

    response = llm.invoke(
        f"""
        Execute this plan.

        {state["research_plan"]}

        Produce:

        - Business Overview
        - Revenue Streams
        - Competitive Position
        - Risks
        """
    )

    return {
        "research_notes": response.content
    }