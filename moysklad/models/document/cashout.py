from typing import Any
from moysklad.models.base import BaseDocument

class CashOut(BaseDocument):
    agent: dict[str, Any] | None = None
    operations: list[dict[str, Any]] | None = None
