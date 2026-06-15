from pydantic import BaseModel
from moysklad.models.base import Meta

class Attribute(BaseModel):
    meta: Meta
    id: str | None = None
    name: str | None = None
    type: str | None = None
    required: bool = False
    description: str | None = None
