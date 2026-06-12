from moysklad.models.base import BaseEntity

class Store(BaseEntity):
    description: str | None = None
    code: str | None = None
    externalCode: str
    archived: bool = False
    pathName: str | None = None
