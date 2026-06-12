from moysklad.api.base import AsyncEndpoint, SyncEndpoint
from moysklad.models.entity.product import Product
from moysklad.models.entity.counterparty import Counterparty

class AsyncEntityAPI:
    def __init__(self, client):
        self.product = AsyncEndpoint[Product](client, "entity/product", Product)
        self.counterparty = AsyncEndpoint[Counterparty](client, "entity/counterparty", Counterparty)

class SyncEntityAPI:
    def __init__(self, client):
        self.product = SyncEndpoint[Product](client, "entity/product", Product)
        self.counterparty = SyncEndpoint[Counterparty](client, "entity/counterparty", Counterparty)
