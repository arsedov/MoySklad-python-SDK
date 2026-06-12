from moysklad.api.base import AsyncEndpoint, SyncEndpoint
from moysklad.models.retail.retailstore import RetailStore
from moysklad.models.retail.retailshift import RetailShift
from moysklad.models.retail.retaildemand import RetailDemand

class AsyncRetailAPI:
    def __init__(self, client):
        self.retailstore = AsyncEndpoint[RetailStore](client, "entity/retailstore", RetailStore)
        self.retailshift = AsyncEndpoint[RetailShift](client, "entity/retailshift", RetailShift)
        self.retaildemand = AsyncEndpoint[RetailDemand](client, "entity/retaildemand", RetailDemand)

class SyncRetailAPI:
    def __init__(self, client):
        self.retailstore = SyncEndpoint[RetailStore](client, "entity/retailstore", RetailStore)
        self.retailshift = SyncEndpoint[RetailShift](client, "entity/retailshift", RetailShift)
        self.retaildemand = SyncEndpoint[RetailDemand](client, "entity/retaildemand", RetailDemand)
