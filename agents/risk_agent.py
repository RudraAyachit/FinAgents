
from utils.logger import logger

async def risk_agent(state):
    debt_ratio = state["debt"] / max(state["income"], 1)

    score = (
        debt_ratio * 55
        + min(state["missed_payments"] * 10, 40)
    )

    reasons = []

    if debt_ratio > 0.5:
        reasons.append("High debt-to-income ratio")

    if state["missed_payments"] > 2:
        reasons.append("Multiple missed payments")

    score = round(min(score, 100), 2)

    logger.info("Risk agent completed")

    return {
        "risk_score": score,
        "risk_level": (
            "HIGH" if score >= 70
            else "MEDIUM" if score >= 40
            else "LOW"
        ),
        "reasons": reasons
    }
