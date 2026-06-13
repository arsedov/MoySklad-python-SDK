from typing import Any
from moysklad.models.base import BaseDocument

class SalesReturn(BaseDocument):
    agent: dict[str, Any] | None = None
    positions: dict[str, Any] | None = None
