from pydantic import BaseModel
from moysklad.models.base import Meta

class BonusTransaction(BaseModel):
    meta: Meta
    id: str
    accountId: str
    updated: str
    created: str | None = None
    transactionType: str
    bonusValue: int
    agent: dict | None = None
    parentDocument: dict | None = None
