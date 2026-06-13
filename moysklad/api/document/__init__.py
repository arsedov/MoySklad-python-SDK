from moysklad.api.base import AsyncEndpoint, SyncEndpoint
from moysklad.models.document.customerorder import CustomerOrder
from moysklad.models.document.demand import Demand
from moysklad.models.document.invoiceout import InvoiceOut
from moysklad.models.document.paymentin import PaymentIn
from moysklad.models.document.supply import Supply
from moysklad.models.document.purchaseorder import PurchaseOrder
from moysklad.models.document.cashin import CashIn
from moysklad.models.document.cashout import CashOut
from moysklad.models.document.salesreturn import SalesReturn
from moysklad.models.document.purchasereturn import PurchaseReturn
from moysklad.models.document.retailsalesreturn import RetailSalesReturn
from moysklad.models.document.inventory import Inventory
from moysklad.models.document.move import Move
from moysklad.models.document.loss import Loss
from moysklad.models.document.enter import Enter
from moysklad.models.document.invoicein import InvoiceIn
from moysklad.models.document.paymentout import PaymentOut
from moysklad.models.document.prepayment import Prepayment
from moysklad.models.document.prepaymentreturn import PrepaymentReturn
from moysklad.models.document.retaildrawercashin import RetailDrawerCashIn
from moysklad.models.document.retaildrawercashout import RetailDrawerCashOut
from moysklad.models.document.facturein import FactureIn
from moysklad.models.document.factureout import FactureOut
from moysklad.models.document.pricelist import PriceList
from moysklad.models.document.internalorder import InternalOrder
from moysklad.models.document.commissionreportin import CommissionReportIn
from moysklad.models.document.commissionreportout import CommissionReportOut
from moysklad.models.document.processing import Processing
from moysklad.models.document.processingorder import ProcessingOrder
from moysklad.models.document.processingplan import ProcessingPlan

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
        self.salesreturn = AsyncEndpoint[SalesReturn](client, "entity/salesreturn", SalesReturn)
        self.purchasereturn = AsyncEndpoint[PurchaseReturn](client, "entity/purchasereturn", PurchaseReturn)
        self.retailsalesreturn = AsyncEndpoint[RetailSalesReturn](client, "entity/retailsalesreturn", RetailSalesReturn)
        self.inventory = AsyncEndpoint[Inventory](client, "entity/inventory", Inventory)
        self.move = AsyncEndpoint[Move](client, "entity/move", Move)
        self.loss = AsyncEndpoint[Loss](client, "entity/loss", Loss)
        self.enter = AsyncEndpoint[Enter](client, "entity/enter", Enter)
        self.invoicein = AsyncEndpoint[InvoiceIn](client, "entity/invoicein", InvoiceIn)
        self.paymentout = AsyncEndpoint[PaymentOut](client, "entity/paymentout", PaymentOut)
        self.prepayment = AsyncEndpoint[Prepayment](client, "entity/prepayment", Prepayment)
        self.prepaymentreturn = AsyncEndpoint[PrepaymentReturn](client, "entity/prepaymentreturn", PrepaymentReturn)
        self.retaildrawercashin = AsyncEndpoint[RetailDrawerCashIn](client, "entity/retaildrawercashin", RetailDrawerCashIn)
        self.retaildrawercashout = AsyncEndpoint[RetailDrawerCashOut](client, "entity/retaildrawercashout", RetailDrawerCashOut)
        self.facturein = AsyncEndpoint[FactureIn](client, "entity/facturein", FactureIn)
        self.factureout = AsyncEndpoint[FactureOut](client, "entity/factureout", FactureOut)
        self.pricelist = AsyncEndpoint[PriceList](client, "entity/pricelist", PriceList)
        self.internalorder = AsyncEndpoint[InternalOrder](client, "entity/internalorder", InternalOrder)
        self.commissionreportin = AsyncEndpoint[CommissionReportIn](client, "entity/commissionreportin", CommissionReportIn)
        self.commissionreportout = AsyncEndpoint[CommissionReportOut](client, "entity/commissionreportout", CommissionReportOut)
        self.processing = AsyncEndpoint[Processing](client, "entity/processing", Processing)
        self.processingorder = AsyncEndpoint[ProcessingOrder](client, "entity/processingorder", ProcessingOrder)
        self.processingplan = AsyncEndpoint[ProcessingPlan](client, "entity/processingplan", ProcessingPlan)

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

        self.salesreturn = SyncEndpoint[SalesReturn](client, "entity/salesreturn", SalesReturn)
        self.purchasereturn = SyncEndpoint[PurchaseReturn](client, "entity/purchasereturn", PurchaseReturn)
        self.retailsalesreturn = SyncEndpoint[RetailSalesReturn](client, "entity/retailsalesreturn", RetailSalesReturn)
        self.inventory = SyncEndpoint[Inventory](client, "entity/inventory", Inventory)
        self.move = SyncEndpoint[Move](client, "entity/move", Move)
        self.loss = SyncEndpoint[Loss](client, "entity/loss", Loss)
        self.enter = SyncEndpoint[Enter](client, "entity/enter", Enter)
        self.invoicein = SyncEndpoint[InvoiceIn](client, "entity/invoicein", InvoiceIn)
        self.paymentout = SyncEndpoint[PaymentOut](client, "entity/paymentout", PaymentOut)
        self.prepayment = SyncEndpoint[Prepayment](client, "entity/prepayment", Prepayment)
        self.prepaymentreturn = SyncEndpoint[PrepaymentReturn](client, "entity/prepaymentreturn", PrepaymentReturn)
        self.retaildrawercashin = SyncEndpoint[RetailDrawerCashIn](client, "entity/retaildrawercashin", RetailDrawerCashIn)
        self.retaildrawercashout = SyncEndpoint[RetailDrawerCashOut](client, "entity/retaildrawercashout", RetailDrawerCashOut)
        self.facturein = SyncEndpoint[FactureIn](client, "entity/facturein", FactureIn)
        self.factureout = SyncEndpoint[FactureOut](client, "entity/factureout", FactureOut)
        self.pricelist = SyncEndpoint[PriceList](client, "entity/pricelist", PriceList)
        self.internalorder = SyncEndpoint[InternalOrder](client, "entity/internalorder", InternalOrder)
        self.commissionreportin = SyncEndpoint[CommissionReportIn](client, "entity/commissionreportin", CommissionReportIn)
        self.commissionreportout = SyncEndpoint[CommissionReportOut](client, "entity/commissionreportout", CommissionReportOut)
        self.processing = SyncEndpoint[Processing](client, "entity/processing", Processing)
        self.processingorder = SyncEndpoint[ProcessingOrder](client, "entity/processingorder", ProcessingOrder)
        self.processingplan = SyncEndpoint[ProcessingPlan](client, "entity/processingplan", ProcessingPlan)