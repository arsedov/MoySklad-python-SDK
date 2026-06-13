from typing import Any
from moysklad.models.base import BaseEntity

class Contract(BaseEntity):
    description: str | None = None
