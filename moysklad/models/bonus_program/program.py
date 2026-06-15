from pydantic import BaseModel
from moysklad.models.base import Meta

class BonusProgram(BaseModel):
    meta: Meta
    id: str | None = None
    accountId: str | None = None
    name: str | None = None
    active: bool | None = None
    earnRateRoublesToPoint: int | None = None
    spendRatePointsToRouble: int | None = None
    maxPaidRatePercents: int | None = None
