from typing import Generic, TypeVar, Any
from pydantic import BaseModel

T = TypeVar("T")

class Meta(BaseModel):
    href: str
    metadataHref: str | None = None
    type: str
    mediaType: str
    uuidHref: str | None = None
    downloadHref: str | None = None
    # Поля пагинации присутствуют в meta списков.
    size: int | None = None
    limit: int | None = None
    offset: int | None = None

class ContextEmployee(BaseModel):
    meta: Meta

class Context(BaseModel):
    employee: ContextEmployee | None = None

class ListResponse(BaseModel, Generic[T]):
    context: Context | None = None
    meta: Meta
    rows: list[T] = []

class BaseEntity(BaseModel):
    # Состав полей в ответах МойСклад зависит от тарифа/типа сущности,
    # поэтому при чтении всё, кроме meta, считаем опциональным.
    meta: Meta
    id: str | None = None
    accountId: str | None = None
    updated: str | None = None
    name: str | None = None

class BaseDocument(BaseEntity):
    moment: str | None = None
    applicable: bool | None = None
    sum: float | None = None
    description: str | None = None
    state: dict[str, Any] | None = None
    organization: dict[str, Any] | None = None
