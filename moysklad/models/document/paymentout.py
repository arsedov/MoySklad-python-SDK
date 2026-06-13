from typing import Any
from moysklad.models.base import BaseDocument

class PaymentOut(BaseDocument):
    agent: dict[str, Any] | None = None
    positions: dict[str, Any] | None = None
