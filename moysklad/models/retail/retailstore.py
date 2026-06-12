from moysklad.models.base import BaseEntity

class RetailStore(BaseEntity):
    description: str | None = None
    code: str | None = None
    externalCode: str
    archived: bool = False
    controlCashierChecks: bool = False
    controlDiscountMarkup: bool = False
    discountEnable: bool = False
    issueOrders: bool = False
    allowCreateProducts: bool = False
