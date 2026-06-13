from typing import Any
from moysklad.models.base import BaseDocument

class Prepayment(BaseDocument):
    agent: dict[str, Any] | None = None
    positions: dict[str, Any] | None = None
