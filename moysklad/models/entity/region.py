from typing import Any
from moysklad.models.base import BaseEntity

class Region(BaseEntity):
    description: str | None = None
