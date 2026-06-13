from typing import Any
from moysklad.models.base import BaseEntity

class Assortment(BaseEntity):
    description: str | None = None
