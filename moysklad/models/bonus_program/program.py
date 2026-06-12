from pydantic import BaseModel
from moysklad.models.base import Meta

class BonusProgram(BaseModel):
    meta: Meta
    id: str
    accountId: str
    name: str
    active: bool
    earnRateRoublesToPoint: int | None = None
    spendRatePointsToRouble: int | None = None
    maxPaidRatePercents: int | None = None
