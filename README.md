
# Financial Multi-Agent Risk Intelligence System 

An enterprise-style AI orchestration platform for financial risk intelligence using FastAPI + LangGraph.

## Features

- Real LangGraph orchestration
- Async multi-agent execution
- Credit risk analysis
- Fraud detection engine
- Spending behavior analytics
- Explainability layer
- Input validation with Pydantic
- Structured logging
- Dockerized deployment
- PostgreSQL-ready architecture
- CI/CD support
- ML-ready pipeline structure

---

## Architecture

```text
Request
  ↓
Validation Layer
  ↓
LangGraph Workflow
  ↓
 ┌─────────────┬──────────────┬──────────────┐
 ↓             ↓              ↓
Risk Agent   Fraud Agent   Behavior Agent
 └─────────────┴──────────────┘
               ↓
          Supervisor
               ↓
          Final Decision
```

---

## Tech Stack

- FastAPI
- LangGraph
- PostgreSQL
- SQLAlchemy
- Docker
- Pytest
- AsyncIO

---

## Run Locally

```bash
docker-compose up --build
```

Swagger Docs:

```bash
http://localhost:8000/docs
```

---

## Sample API Request

```json
{
  "income": 5000,
  "debt": 2500,
  "monthly_spending": 3200,
  "missed_payments": 1,
  "transaction_velocity": 5,
  "avg_transaction_size": 1200
}
```

---

## Resume Highlights

- Built a real-time multi-agent financial intelligence system using LangGraph and FastAPI
- Implemented asynchronous agent orchestration with explainable AI workflows
- Developed fraud detection and behavioral analytics pipelines
- Designed scalable microservice-ready backend architecture
- Added validation, logging, CI-ready testing, and containerized deployment

