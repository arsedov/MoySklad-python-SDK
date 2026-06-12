from pydantic import BaseModel
from moysklad.models.base import BaseEntity

class Employee(BaseEntity):
    firstName: str | None = None
    lastName: str | None = None
    middleName: str | None = None
    email: str | None = None
    phone: str | None = None
    inn: str | None = None
    position: str | None = None
    archived: bool = False
