from typing import Generic, TypeVar, Any
from pydantic import BaseModel, Field

T = TypeVar("T")

class Meta(BaseModel):
    href: str
    metadataHref: str | None = None
    type: str
    mediaType: str
    uuidHref: str | None = None
    downloadHref: str | None = None

class ContextEmployee(BaseModel):
    meta: Meta

class Context(BaseModel):
    employee: ContextEmployee | None = None

class ListResponse(BaseModel, Generic[T]):
    context: Context
    meta: Meta
    rows: list[T]
