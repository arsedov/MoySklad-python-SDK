from typing import Any
from moysklad.models.base import BaseDocument

class InvoiceOut(BaseDocument):
    agent: dict[str, Any]
    paymentPlannedMoment: str | None = None
    customerOrder: dict[str, Any] | None = None
    demands: list[dict[str, Any]] | None = None
    positions: dict[str, Any] | None = None
