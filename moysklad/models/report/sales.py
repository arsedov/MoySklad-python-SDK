from pydantic import BaseModel
from moysklad.models.base import Meta

class SalesRow(BaseModel):
    meta: Meta
    name: str | None = None
    code: str | None = None
    article: str | None = None
    sellQuantity: float | None = None
    sellPrice: float | None = None
    sellCost: float | None = None
    sellSum: float | None = None
    returnQuantity: float | None = None
    returnPrice: float | None = None
    returnCost: float | None = None
    returnSum: float | None = None
    profit: float | None = None
    margin: float | None = None
