from moysklad.api.base import AsyncEndpoint, SyncEndpoint
from moysklad.models.document.customerorder import CustomerOrder
from moysklad.models.document.demand import Demand

class AsyncDocumentAPI:
    def __init__(self, client):
        self.customerorder = AsyncEndpoint[CustomerOrder](client, "entity/customerorder", CustomerOrder)
        self.demand = AsyncEndpoint[Demand](client, "entity/demand", Demand)

class SyncDocumentAPI:
    def __init__(self, client):
        self.customerorder = SyncEndpoint[CustomerOrder](client, "entity/customerorder", CustomerOrder)
        self.demand = SyncEndpoint[Demand](client, "entity/demand", Demand)
