from pydantic import BaseModel
from moysklad.models.base import BaseEntity

class Currency(BaseEntity):
    rate: float
    multiplicity: int
    default: bool
    isoCode: str
    code: str | None = None
    archived: bool = False
