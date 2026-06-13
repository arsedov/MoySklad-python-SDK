from typing import Any
from moysklad.models.base import BaseEntity

class CustomEntity(BaseEntity):
    description: str | None = None
