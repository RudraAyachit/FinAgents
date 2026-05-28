
from fastapi import FastAPI, HTTPException
from schemas.user import UserData
from graphs.workflow import run_financial_workflow

app = FastAPI(
    title="Financial Multi-Agent Risk Intelligence System",
    version="2.0.0"
)


@app.get("/")
async def root():
    return {
        "status": "running",
        "system": "financial-risk-intelligence"
    }


@app.post("/risk-analysis")
async def risk_analysis(user: UserData):
    try:
        result = await run_financial_workflow(user.model_dump())
        return result
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Workflow execution failed: {str(exc)}"
        )
