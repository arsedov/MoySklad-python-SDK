from moysklad.api.base import AsyncEndpoint, SyncEndpoint
from moysklad.models.entity.product import Product
from moysklad.models.entity.counterparty import Counterparty
from moysklad.models.entity.organization import Organization
from moysklad.models.entity.store import Store
from moysklad.models.entity.employee import Employee
from moysklad.models.entity.currency import Currency
from moysklad.models.entity.project import Project
from moysklad.models.entity.task import Task
from moysklad.models.entity.service import Service
from moysklad.models.entity.variant import Variant
from moysklad.models.entity.bundle import Bundle
from moysklad.models.entity.productfolder import ProductFolder
from moysklad.models.entity.uom import Uom
from moysklad.models.entity.consignment import Consignment
from moysklad.models.entity.contract import Contract
from moysklad.models.entity.expenseitem import ExpenseItem
from moysklad.models.entity.group import Group
from moysklad.models.entity.region import Region
from moysklad.models.entity.country import Country
from moysklad.models.entity.customentity import CustomEntity
from moysklad.models.entity.assortment import Assortment
from moysklad.models.entity.taxrate import TaxRate
from moysklad.models.entity.saleschannel import SalesChannel
from moysklad.models.entity.bonustransaction import BonusTransaction
from moysklad.models.entity.discount import Discount

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
        self.service = AsyncEndpoint[Service](client, "entity/service", Service)
        self.variant = AsyncEndpoint[Variant](client, "entity/variant", Variant)
        self.bundle = AsyncEndpoint[Bundle](client, "entity/bundle", Bundle)
        self.productfolder = AsyncEndpoint[ProductFolder](client, "entity/productfolder", ProductFolder)
        self.uom = AsyncEndpoint[Uom](client, "entity/uom", Uom)
        self.consignment = AsyncEndpoint[Consignment](client, "entity/consignment", Consignment)
        self.contract = AsyncEndpoint[Contract](client, "entity/contract", Contract)
        self.expenseitem = AsyncEndpoint[ExpenseItem](client, "entity/expenseitem", ExpenseItem)
        self.group = AsyncEndpoint[Group](client, "entity/group", Group)
        self.region = AsyncEndpoint[Region](client, "entity/region", Region)
        self.country = AsyncEndpoint[Country](client, "entity/country", Country)
        self.customentity = AsyncEndpoint[CustomEntity](client, "entity/customentity", CustomEntity)
        self.assortment = AsyncEndpoint[Assortment](client, "entity/assortment", Assortment)
        self.taxrate = AsyncEndpoint[TaxRate](client, "entity/taxrate", TaxRate)
        self.saleschannel = AsyncEndpoint[SalesChannel](client, "entity/saleschannel", SalesChannel)
        self.bonustransaction = AsyncEndpoint[BonusTransaction](client, "entity/bonustransaction", BonusTransaction)
        self.discount = AsyncEndpoint[Discount](client, "entity/discount", Discount)

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

        self.service = SyncEndpoint[Service](client, "entity/service", Service)
        self.variant = SyncEndpoint[Variant](client, "entity/variant", Variant)
        self.bundle = SyncEndpoint[Bundle](client, "entity/bundle", Bundle)
        self.productfolder = SyncEndpoint[ProductFolder](client, "entity/productfolder", ProductFolder)
        self.uom = SyncEndpoint[Uom](client, "entity/uom", Uom)
        self.consignment = SyncEndpoint[Consignment](client, "entity/consignment", Consignment)
        self.contract = SyncEndpoint[Contract](client, "entity/contract", Contract)
        self.expenseitem = SyncEndpoint[ExpenseItem](client, "entity/expenseitem", ExpenseItem)
        self.group = SyncEndpoint[Group](client, "entity/group", Group)
        self.region = SyncEndpoint[Region](client, "entity/region", Region)
        self.country = SyncEndpoint[Country](client, "entity/country", Country)
        self.customentity = SyncEndpoint[CustomEntity](client, "entity/customentity", CustomEntity)
        self.assortment = SyncEndpoint[Assortment](client, "entity/assortment", Assortment)
        self.taxrate = SyncEndpoint[TaxRate](client, "entity/taxrate", TaxRate)
        self.saleschannel = SyncEndpoint[SalesChannel](client, "entity/saleschannel", SalesChannel)
        self.bonustransaction = SyncEndpoint[BonusTransaction](client, "entity/bonustransaction", BonusTransaction)
        self.discount = SyncEndpoint[Discount](client, "entity/discount", Discount)