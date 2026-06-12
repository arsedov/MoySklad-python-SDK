from moysklad.models.base import BaseDocument
from typing import Any

class RetailShift(BaseDocument):
    retailStore: dict[str, Any] | None = None
    closeDate: str | None = None
    proceedsNoCash: float | None = None
    proceedsCash: float | None = None
    receivedNoCash: float | None = None
    receivedCash: float | None = None
