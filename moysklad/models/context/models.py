from pydantic import BaseModel
from moysklad.models.base import Meta
from typing import Any

class CompanySettings(BaseModel):
    meta: Meta
    currency: dict[str, Any] | None = None
    priceTypes: list[dict[str, Any]] | None = None
    discountStrategy: str | None = None
    globalSyncState: dict[str, Any] | None = None

class ContextEmployee(BaseModel):
    meta: Meta
    employee: dict[str, Any] | None = None
