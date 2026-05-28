
async def supervisor(results):
    overall = "LOW"

    if results["risk"]["risk_score"] >= 70:
        overall = "HIGH"

    if results["fraud"]["fraud_flag"]:
        overall = "CRITICAL"

    return {
        "overall_assessment": overall,
        "recommendation": (
            "Manual review required"
            if overall in ["HIGH", "CRITICAL"]
            else "Auto-approved"
        ),
        "explainability": {
            "risk_reasons": results["risk"]["reasons"],
            "behavior_profile": results["behavior"]["behavior_profile"]
        }
    }
