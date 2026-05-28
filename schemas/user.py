
from pydantic import BaseModel, Field, computed_field

class UserData(BaseModel):
    income: float = Field(gt=0)
    debt: float = Field(ge=0)
    monthly_spending: float = Field(ge=0)
    missed_payments: int = Field(ge=0, le=24)
    transaction_velocity: int = Field(ge=0, le=100)
    avg_transaction_size: float = Field(default=0, ge=0)

    @computed_field
    @property
    def debt_ratio(self) -> float:
        return round(self.debt / self.income, 2)
