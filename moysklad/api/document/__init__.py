from moysklad.api.base import AsyncEndpoint, SyncEndpoint
from moysklad.models.document.customerorder import CustomerOrder
from moysklad.models.document.demand import Demand
from moysklad.models.document.invoiceout import InvoiceOut
from moysklad.models.document.paymentin import PaymentIn
from moysklad.models.document.supply import Supply
from moysklad.models.document.purchaseorder import PurchaseOrder
from moysklad.models.document.cashin import CashIn
from moysklad.models.document.cashout import CashOut

class AsyncDocumentAPI:
    def __init__(self, client):
        self.customerorder = AsyncEndpoint[CustomerOrder](client, "entity/customerorder", CustomerOrder)
        self.demand = AsyncEndpoint[Demand](client, "entity/demand", Demand)
        self.invoiceout = AsyncEndpoint[InvoiceOut](client, "entity/invoiceout", InvoiceOut)
        self.paymentin = AsyncEndpoint[PaymentIn](client, "entity/paymentin", PaymentIn)
        self.supply = AsyncEndpoint[Supply](client, "entity/supply", Supply)
        self.purchaseorder = AsyncEndpoint[PurchaseOrder](client, "entity/purchaseorder", PurchaseOrder)
        self.cashin = AsyncEndpoint[CashIn](client, "entity/cashin", CashIn)
        self.cashout = AsyncEndpoint[CashOut](client, "entity/cashout", CashOut)

class SyncDocumentAPI:
    def __init__(self, client):
        self.customerorder = SyncEndpoint[CustomerOrder](client, "entity/customerorder", CustomerOrder)
        self.demand = SyncEndpoint[Demand](client, "entity/demand", Demand)
        self.invoiceout = SyncEndpoint[InvoiceOut](client, "entity/invoiceout", InvoiceOut)
        self.paymentin = SyncEndpoint[PaymentIn](client, "entity/paymentin", PaymentIn)
        self.supply = SyncEndpoint[Supply](client, "entity/supply", Supply)
        self.purchaseorder = SyncEndpoint[PurchaseOrder](client, "entity/purchaseorder", PurchaseOrder)
        self.cashin = SyncEndpoint[CashIn](client, "entity/cashin", CashIn)
        self.cashout = SyncEndpoint[CashOut](client, "entity/cashout", CashOut)
