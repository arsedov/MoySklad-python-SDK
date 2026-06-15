from moysklad.models.base import BaseEntity

class Store(BaseEntity):
    description: str | None = None
    code: str | None = None
    externalCode: str | None = None
    archived: bool = False
    pathName: str | None = None
