from config import PROJECT_ID
from config import LOCATION

from langchain_google_vertexai import ChatVertexAI


llm = ChatVertexAI(
    model="gemini-2.5-flash",
    project=PROJECT_ID,
    location=LOCATION
)


def writer_node(state):

    financial_analysis = state.get(
        "financial_analysis",
        "No financial analysis performed."
    )

    response = llm.invoke(
        f"""
        Create a professional investment report.

        Research Notes:

        {state["research_notes"]}

        Financial Analysis:

        {financial_analysis}

        Include:

        Executive Summary

        Business Overview

        Bull Case

        Bear Case

        Risks

        Final Recommendation
        """
    )

    return {
        "report": response.content
    }