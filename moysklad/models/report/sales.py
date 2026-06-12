from pydantic import BaseModel
from moysklad.models.base import Meta

class SalesRow(BaseModel):
    meta: Meta
    name: str
    code: str | None = None
    article: str | None = None
    sellQuantity: float
    sellPrice: float
    sellCost: float
    sellSum: float
    returnQuantity: float
    returnPrice: float
    returnCost: float
    returnSum: float
    profit: float
    margin: float
