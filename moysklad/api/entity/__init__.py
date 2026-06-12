from moysklad.api.base import AsyncEndpoint, SyncEndpoint
from moysklad.models.entity.product import Product
from moysklad.models.entity.counterparty import Counterparty
from moysklad.models.entity.organization import Organization
from moysklad.models.entity.store import Store

class AsyncEntityAPI:
    def __init__(self, client):
        self.product = AsyncEndpoint[Product](client, "entity/product", Product)
        self.counterparty = AsyncEndpoint[Counterparty](client, "entity/counterparty", Counterparty)
        self.organization = AsyncEndpoint[Organization](client, "entity/organization", Organization)
        self.store = AsyncEndpoint[Store](client, "entity/store", Store)

class SyncEntityAPI:
    def __init__(self, client):
        self.product = SyncEndpoint[Product](client, "entity/product", Product)
        self.counterparty = SyncEndpoint[Counterparty](client, "entity/counterparty", Counterparty)
        self.organization = SyncEndpoint[Organization](client, "entity/organization", Organization)
        self.store = SyncEndpoint[Store](client, "entity/store", Store)
