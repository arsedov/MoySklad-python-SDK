from pydantic import BaseModel
from moysklad.models.base import Meta
from typing import Any

class StockRow(BaseModel):
    meta: Meta
    name: str
    code: str | None = None
    article: str | None = None
    stock: float
    inTransit: float
    reserve: float
    quantity: float
    price: float | None = None
    salePrice: float | None = None
    folder: dict[str, Any] | None = None
