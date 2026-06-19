from fastapi import FastAPI

from graph import graph

from models import AnalysisRequest


app = FastAPI()


@app.get("/")
def health():

    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze(payload: AnalysisRequest):

    result = graph.invoke(
        {
            "question": payload.question,
            "retry_count": 0
        }
    )

    return {
    "research_plan":
        result.get(
            "research_plan",
            ""
        ),

    "research_notes":
        result.get(
            "research_notes",
            ""
        ),

    "financial_analysis":
        result.get(
            "financial_analysis",
            ""
        ),

    "report":
        result.get(
            "report",
            ""
        )
    }