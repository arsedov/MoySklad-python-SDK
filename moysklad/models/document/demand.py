from pydantic import BaseModel
from typing import Any
from moysklad.models.base import Meta

class Demand(BaseModel):
    meta: Meta
    id: str
    accountId: str
    name: str
    description: str | None = None
    updated: str
    moment: str
    applicable: bool
    sum: float
    agent: dict[str, Any]
    organization: dict[str, Any]
    customerOrder: dict[str, Any] | None = None
    state: dict[str, Any] | None = None
    positions: dict[str, Any] | None = None
