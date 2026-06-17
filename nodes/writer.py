from config import PROJECT_ID
from config import LOCATION

from langchain_google_vertexai import ChatVertexAI


llm = ChatVertexAI(
    model="gemini-2.5-flash",
    project=PROJECT_ID,
    location=LOCATION
)


def writer_node(state):

    response = llm.invoke(
        f"""
        Create a professional
        investment report.

        Research:

        {state["research_notes"]}

        Financial:

        {state["financial_analysis"]}

        Include:

        Executive Summary

        Bull Case

        Bear Case

        Risks

        Recommendation
        """
    )

    return {
        "report": response.content
    }