from moysklad.models.base import BaseEntity

class Currency(BaseEntity):
    rate: float | None = None
    multiplicity: int | None = None
    default: bool | None = None
    isoCode: str | None = None
    code: str | None = None
    archived: bool = False
