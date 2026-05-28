
from utils.logger import logger

async def fraud_agent(state):
    velocity_score = min(state["transaction_velocity"] * 6, 60)

    anomaly_bonus = 20 if state["avg_transaction_size"] > 2000 else 0

    fraud_probability = round(
        min(velocity_score + anomaly_bonus, 100),
        2
    )

    logger.info("Fraud agent completed")

    return {
        "fraud_probability": fraud_probability,
        "fraud_flag": fraud_probability >= 70,
        "signals": {
            "high_velocity": state["transaction_velocity"] > 10,
            "large_transactions": state["avg_transaction_size"] > 2000
        }
    }
