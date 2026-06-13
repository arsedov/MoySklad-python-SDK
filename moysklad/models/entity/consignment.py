from typing import Any
from moysklad.models.base import BaseEntity

class Consignment(BaseEntity):
    description: str | None = None
