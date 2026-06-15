from typing import Any
from moysklad.models.base import BaseDocument

class Demand(BaseDocument):
    agent: dict[str, Any] | None = None
    customerOrder: dict[str, Any] | None = None
    positions: dict[str, Any] | None = None
