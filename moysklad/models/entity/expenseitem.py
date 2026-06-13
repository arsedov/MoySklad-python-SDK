from typing import Any
from moysklad.models.base import BaseEntity

class ExpenseItem(BaseEntity):
    description: str | None = None
