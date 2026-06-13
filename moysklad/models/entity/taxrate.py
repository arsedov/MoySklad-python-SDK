from typing import Any
from moysklad.models.base import BaseEntity

class TaxRate(BaseEntity):
    description: str | None = None
