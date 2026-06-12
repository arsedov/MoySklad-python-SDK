from moysklad.api.base import AsyncEndpoint, SyncEndpoint
from moysklad.models.entity.product import Product
from moysklad.models.entity.counterparty import Counterparty
from moysklad.models.entity.organization import Organization
from moysklad.models.entity.store import Store
from moysklad.models.entity.employee import Employee
from moysklad.models.entity.currency import Currency
from moysklad.models.entity.project import Project
from moysklad.models.entity.task import Task

class AsyncEntityAPI:
    def __init__(self, client):
        self.product = AsyncEndpoint[Product](client, "entity/product", Product)
        self.counterparty = AsyncEndpoint[Counterparty](client, "entity/counterparty", Counterparty)
        self.organization = AsyncEndpoint[Organization](client, "entity/organization", Organization)
        self.store = AsyncEndpoint[Store](client, "entity/store", Store)
        self.employee = AsyncEndpoint[Employee](client, "entity/employee", Employee)
        self.currency = AsyncEndpoint[Currency](client, "entity/currency", Currency)
        self.project = AsyncEndpoint[Project](client, "entity/project", Project)
        self.task = AsyncEndpoint[Task](client, "entity/task", Task)

class SyncEntityAPI:
    def __init__(self, client):
        self.product = SyncEndpoint[Product](client, "entity/product", Product)
        self.counterparty = SyncEndpoint[Counterparty](client, "entity/counterparty", Counterparty)
        self.organization = SyncEndpoint[Organization](client, "entity/organization", Organization)
        self.store = SyncEndpoint[Store](client, "entity/store", Store)
        self.employee = SyncEndpoint[Employee](client, "entity/employee", Employee)
        self.currency = SyncEndpoint[Currency](client, "entity/currency", Currency)
        self.project = SyncEndpoint[Project](client, "entity/project", Project)
        self.task = SyncEndpoint[Task](client, "entity/task", Task)
