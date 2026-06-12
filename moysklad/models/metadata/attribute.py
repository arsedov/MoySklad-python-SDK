from pydantic import BaseModel
from moysklad.models.base import Meta

class Attribute(BaseModel):
    meta: Meta
    id: str
    name: str
    type: str
    required: bool = False
    description: str | None = None
