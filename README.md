
# FinAgents : Financial Multi-Agent Intelligence System 

An enterprise-style AI orchestration platform for financial intelligence using FastAPI + LangGraph.

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



