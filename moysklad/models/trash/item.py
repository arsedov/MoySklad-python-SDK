from pydantic import BaseModel
from moysklad.models.base import Meta
from typing import Any

class TrashItem(BaseModel):
    meta: Meta
    id: str | None = None
    accountId: str | None = None
    name: str | None = None
    trashed: str | None = None
    trashType: str | None = None
    trashEntity: dict[str, Any] | None = None
