from config import *
from langchain_google_vertexai import ChatVertexAI


llm = ChatVertexAI(
    model="gemini-2.5-flash"
)


def reviewer_node(state):

    response = llm.invoke(
        f"""
        Review this report.

        {state["report"]}

        Score quality from 1-10.

        Return ONLY a number.
        """
    )

    try:
        score = int(response.content.strip())

    except:
        score = 5

    return {
        "review_score": score
    }