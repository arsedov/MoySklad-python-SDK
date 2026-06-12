from typing import Any
from moysklad.models.base import BaseDocument

class PurchaseOrder(BaseDocument):
    agent: dict[str, Any]
    positions: dict[str, Any] | None = None
