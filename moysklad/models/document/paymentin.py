from typing import Any
from moysklad.models.base import BaseDocument

class PaymentIn(BaseDocument):
    agent: dict[str, Any]
    operations: list[dict[str, Any]] | None = None
