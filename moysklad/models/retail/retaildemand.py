from moysklad.models.base import BaseDocument
from typing import Any

class RetailDemand(BaseDocument):
    agent: dict[str, Any]
    retailStore: dict[str, Any] | None = None
    retailShift: dict[str, Any] | None = None
    positions: dict[str, Any] | None = None
    document: dict[str, Any] | None = None
