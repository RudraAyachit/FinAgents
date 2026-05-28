
import pytest

from graphs.workflow import run_financial_workflow


@pytest.mark.asyncio
async def test_workflow():
    data = {
        "income": 5000,
        "debt": 4000,
        "monthly_spending": 4500,
        "missed_payments": 4,
        "transaction_velocity": 8,
        "avg_transaction_size": 2500
    }

    result = await run_financial_workflow(data)

    assert "final" in result
    assert result["risk"]["risk_level"] == "HIGH"
    assert result["fraud"]["fraud_flag"] is True
