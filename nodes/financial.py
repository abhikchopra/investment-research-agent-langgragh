from config import *
from langchain_google_vertexai import ChatVertexAI


llm = ChatVertexAI(
    model="gemini-2.5-flash"
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