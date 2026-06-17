from langgraph.graph import (
    StateGraph,
    END
)

from state import ResearchState

from nodes.planner import planner_node
from nodes.research import research_node
from nodes.financial import financial_node
from nodes.writer import writer_node
from nodes.reviewer import reviewer_node


# --------------------------------------------------
# ROUTER 1
# RESEARCH -> FINANCIAL OR WRITER
# --------------------------------------------------

def route_after_research(state):

    question = state["question"].lower()

    keywords = [
        "investment",
        "stock",
        "valuation",
        "financial",
        "earnings"
    ]

    if any(
        keyword in question
        for keyword in keywords
    ):
        return "financial"

    return "writer"


# --------------------------------------------------
# ROUTER 2
# REVIEW LOOP
# --------------------------------------------------

def route_after_review(state):

    score = state["review_score"]

    retries = state.get(
        "retry_count",
        0
    )

    if score >= 7:
        return END

    if retries >= 1:
        return END

    state["retry_count"] = retries + 1

    return "research"


# --------------------------------------------------
# BUILD GRAPH
# --------------------------------------------------

builder = StateGraph(
    ResearchState
)


# Nodes

builder.add_node(
    "planner",
    planner_node
)

builder.add_node(
    "research",
    research_node
)

builder.add_node(
    "financial",
    financial_node
)

builder.add_node(
    "writer",
    writer_node
)

builder.add_node(
    "reviewer",
    reviewer_node
)


# Entry Point

builder.set_entry_point(
    "planner"
)


# Planner -> Research

builder.add_edge(
    "planner",
    "research"
)


# Research Router

builder.add_conditional_edges(
    "research",
    route_after_research
)


# Financial -> Writer

builder.add_edge(
    "financial",
    "writer"
)


# Writer -> Reviewer

builder.add_edge(
    "writer",
    "reviewer"
)


# Review Loop

builder.add_conditional_edges(
    "reviewer",
    route_after_review
)


graph = builder.compile()


# --------------------------------------------------
# RUN
# --------------------------------------------------

