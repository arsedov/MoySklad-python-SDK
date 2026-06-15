from pydantic import BaseModel
from moysklad.models.base import Meta

class BonusTransaction(BaseModel):
    meta: Meta
    id: str | None = None
    accountId: str | None = None
    updated: str | None = None
    created: str | None = None
    transactionType: str | None = None
    bonusValue: int | None = None
    agent: dict | None = None
    parentDocument: dict | None = None
