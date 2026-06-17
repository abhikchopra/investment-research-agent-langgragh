from typing import TypedDict


class ResearchState(TypedDict):

    question: str

    research_plan: str

    research_notes: str

    financial_analysis: str

    report: str

    review_score: int

    retry_count: int