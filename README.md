# Investment Research Agent - LangGraph

A production-oriented investment research workflow built using **LangGraph**, **Vertex AI (Gemini)**, **FastAPI**, **Docker**, and **Google Cloud Run**.

This project demonstrates how to orchestrate multi-step AI workflows using LangGraph's graph-based architecture while maintaining shared state, dynamic routing, and self-correction patterns.

---

## Objective

The goal of this repository is to rebuild the Investment Research Agent previously implemented using Google ADK and compare two orchestration approaches:

### Repository 1

Google ADK

* SequentialAgent
* Agent-to-Agent orchestration
* Tool Calling
* Cloud Run deployment

### Repository 2 (This Repository)

LangGraph

* StateGraph orchestration
* Shared State
* Conditional Routing
* Reflection Loops
* Retry Logic
* FastAPI
* Docker
* Cloud Run

---

## Architecture

```text
User Question
      ↓

Planner Node
      ↓

Research Node
      ↓

Need Financial Analysis?

 YES          NO
  ↓            ↓

Financial     Writer
    ↓            ↑
    └────────────┘

      ↓

Writer Node
      ↓

Reviewer Node
      ↓

Quality Check

Score >= Threshold?
      ↓

 YES → END

 NO  → Research Again
```

---

## Core LangGraph Concepts Demonstrated

### 1. Shared State

All workflow steps operate on a common state object.

State contains:

* question
* research_plan
* research_notes
* financial_analysis
* report
* review_score
* retry_count

This acts as shared memory across the workflow.

---

### 2. Nodes

Each node performs a specific task.

| Node      | Responsibility                           |
| --------- | ---------------------------------------- |
| Planner   | Creates research plan                    |
| Research  | Collects business and market information |
| Financial | Performs investment analysis             |
| Writer    | Generates final report                   |
| Reviewer  | Evaluates report quality                 |

---

### 3. Edges

Workflow transitions are explicitly defined using LangGraph edges.

Example:

Planner → Research → Financial → Writer

Unlike ADK, workflow orchestration is fully controlled by the developer.

---

### 4. Conditional Routing

The workflow can dynamically choose the next step.

Example:

Investment Questions

Research → Financial → Writer

Informational Questions

Research → Writer

This demonstrates graph-based decision making.

---

### 5. Reflection Loop

A reviewer node evaluates report quality.

If quality is insufficient:

Reviewer → Research → Writer → Reviewer

This introduces self-correction and iterative improvement.

---

### 6. Retry Protection

A retry counter prevents infinite loops and ensures workflow termination.

---

## Technology Stack

### AI & Orchestration

* LangGraph
* LangChain
* Vertex AI
* Gemini 2.5 Flash

### Backend

* FastAPI
* Uvicorn

### Infrastructure

* Docker
* Google Cloud Run
* Artifact Registry

### Development

* Python 3.12
* GitHub
* GitHub Actions

---

## API

### Analyze Investment Opportunity

POST `/analyze`

Request:

```json
{
  "question": "Analyze Microsoft as an investment opportunity"
}
```

Response:

```json
{
  "report": "..."
}
```

---

## Local Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
uvicorn app:app --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## Deployment

Containerized using Docker and deployed to Google Cloud Run.

Key deployment concepts:

* Vertex AI authentication
* Environment variables
* Docker containerization
* Cloud Run serverless deployment
* Artifact Registry image management

---

## Key Learnings

This repository demonstrates the concepts most commonly associated with production LangGraph systems:

* State Management
* Workflow Orchestration
* Conditional Routing
* Reflection Loops
* Retry Logic
* Vertex AI Integration
* FastAPI APIs
* Docker Containerization
* Cloud Deployment

The primary purpose of this repository is to understand how LangGraph differs from Google ADK while solving the same business problem.
