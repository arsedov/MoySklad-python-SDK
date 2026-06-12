from moysklad.models.base import BaseEntity

class Counterparty(BaseEntity):
    owner: dict | None = None
    shared: bool = False
    group: dict | None = None
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
