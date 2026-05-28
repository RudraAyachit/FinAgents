
import asyncio
from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.risk_agent import risk_agent
from agents.fraud_agent import fraud_agent
from agents.behavior_agent import behavior_agent
from agents.supervisor import supervisor


class FinancialState(TypedDict, total=False):
    income: float
    debt: float
    monthly_spending: float
    missed_payments: int
    transaction_velocity: int
    avg_transaction_size: float
    risk: dict
    fraud: dict
    behavior: dict
    final: dict


async def parallel_agents(state: FinancialState):
    risk, fraud, behavior = await asyncio.gather(
        risk_agent(state),
        fraud_agent(state),
        behavior_agent(state)
    )

    return {
        **state,
        "risk": risk,
        "fraud": fraud,
        "behavior": behavior
    }


async def finalize(state: FinancialState):
    final = await supervisor(state)

    return {
        **state,
        "final": final
    }


graph = StateGraph(FinancialState)

graph.add_node("parallel_agents", parallel_agents)
graph.add_node("finalize", finalize)

graph.set_entry_point("parallel_agents")
graph.add_edge("parallel_agents", "finalize")
graph.add_edge("finalize", END)

workflow = graph.compile()


async def run_financial_workflow(state):
    return await workflow.ainvoke(state)
