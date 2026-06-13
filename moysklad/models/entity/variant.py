from typing import Any
from moysklad.models.base import BaseEntity

class Variant(BaseEntity):
    description: str | None = None
