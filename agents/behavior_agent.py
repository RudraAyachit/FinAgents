
from utils.logger import logger

async def behavior_agent(state):
    spend_ratio = state["monthly_spending"] / max(state["income"], 1)

    profile = (
        "HIGH_RISK"
        if spend_ratio > 0.9
        else "IMPULSIVE"
        if spend_ratio > 0.75
        else "CONTROLLED"
    )

    logger.info("Behavior agent completed")

    return {
        "spending_ratio": round(spend_ratio, 2),
        "behavior_profile": profile
    }
