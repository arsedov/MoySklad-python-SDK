from pydantic import BaseModel
from moysklad.models.base import BaseEntity

class Project(BaseEntity):
    code: str | None = None
    description: str | None = None
    archived: bool = False
