from pydantic import BaseModel
from moysklad.models.base import Meta

class Counterparty(BaseModel):
    meta: Meta
    id: str
    accountId: str
    owner: dict | None = None
    shared: bool = False
    group: dict | None = None
    updated: str
    name: str
    description: str | None = None
    code: str | None = None
    externalCode: str
    archived: bool = False
    companyType: str
    inn: str | None = None
    kpp: str | None = None
    legalTitle: str | None = None
    email: str | None = None
    phone: str | None = None
