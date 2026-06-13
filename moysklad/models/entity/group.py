from typing import Any
from moysklad.models.base import BaseEntity

class Group(BaseEntity):
    description: str | None = None
