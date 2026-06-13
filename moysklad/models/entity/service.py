from typing import Any
from moysklad.models.base import BaseEntity

class Service(BaseEntity):
    description: str | None = None
