from config import PROJECT_ID
from config import LOCATION

from langchain_google_vertexai import ChatVertexAI


llm = ChatVertexAI(
    model="gemini-2.5-flash",
    project=PROJECT_ID,
    location=LOCATION
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