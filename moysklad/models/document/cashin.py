from typing import Any
from moysklad.models.base import BaseDocument

class CashIn(BaseDocument):
    agent: dict[str, Any] | None = None
    operations: list[dict[str, Any]] | None = None
