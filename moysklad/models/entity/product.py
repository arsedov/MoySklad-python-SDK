from moysklad.models.base import BaseEntity

class Product(BaseEntity):
    owner: dict | None = None
    shared: bool = False
    group: dict | None = None
    description: str | None = None
    code: str | None = None
    externalCode: str
    archived: bool = False
    pathName: str | None = None
    article: str | None = None
    weight: float | None = None
    volume: float | None = None
