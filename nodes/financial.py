from config import PROJECT_ID
from config import LOCATION

from langchain_google_vertexai import ChatVertexAI


llm = ChatVertexAI(
    model="gemini-2.5-flash",
    project=PROJECT_ID,
    location=LOCATION
)


def financial_node(state):

    response = llm.invoke(
        f"""
        Analyze:

        {state["research_notes"]}

        Produce:

        Revenue Analysis

        Profitability

        Valuation

        Investment View
        """
    )

    return {
        "financial_analysis": response.content
    }