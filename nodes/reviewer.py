from config import PROJECT_ID
from config import LOCATION

from langchain_google_vertexai import ChatVertexAI


llm = ChatVertexAI(
    model="gemini-2.5-flash",
    project=PROJECT_ID,
    location=LOCATION
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