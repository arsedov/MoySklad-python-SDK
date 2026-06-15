from typing import Any
from moysklad.models.base import BaseDocument

class Supply(BaseDocument):
    agent: dict[str, Any] | None = None
    purchaseOrder: dict[str, Any] | None = None
    positions: dict[str, Any] | None = None
