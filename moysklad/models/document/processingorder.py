from typing import Any
from moysklad.models.base import BaseDocument

class ProcessingOrder(BaseDocument):
    agent: dict[str, Any] | None = None
    positions: dict[str, Any] | None = None
