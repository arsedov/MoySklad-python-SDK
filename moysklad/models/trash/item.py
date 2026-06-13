from pydantic import BaseModel
from moysklad.models.base import Meta
from typing import Any

class TrashItem(BaseModel):
    meta: Meta
    id: str
    accountId: str
    name: str | None = None
    trashed: str
    trashType: str
    trashEntity: dict[str, Any] | None = None
