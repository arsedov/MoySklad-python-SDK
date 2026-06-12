from typing import Any, Generic, TypeVar, AsyncGenerator, Generator
from moysklad.models.base import ListResponse
from moysklad.models.report.stock import StockRow
from moysklad.models.report.sales import SalesRow
from moysklad.utils.filters import Filter
from pydantic import TypeAdapter

T = TypeVar("T")

class AsyncReportEndpoint(Generic[T]):
    def __init__(self, client: Any, path: str, model: Any):
        self.client = client
        self.path = path
        self.model = model

    async def list(self, limit: int = 1000, offset: int = 0, filter: str | Filter | None = None) -> ListResponse[T]:
        params = {"limit": limit, "offset": offset}
        if filter:
            params["filter"] = str(filter)
            
        data = await self.client.get(self.path, params=params)
        adapter = TypeAdapter(ListResponse[self.model])
        return adapter.validate_python(data)

    async def iter_all(self, filter: str | Filter | None = None, chunk_size: int = 1000) -> AsyncGenerator[T, None]:
        offset = 0
        while True:
            response = await self.list(limit=chunk_size, offset=offset, filter=filter)
            for row in response.rows:
                yield row
            if len(response.rows) < chunk_size:
                break
            offset += chunk_size

class SyncReportEndpoint(Generic[T]):
    def __init__(self, client: Any, path: str, model: Any):
        self.client = client
        self.path = path
        self.model = model

    def list(self, limit: int = 1000, offset: int = 0, filter: str | Filter | None = None) -> ListResponse[T]:
        params = {"limit": limit, "offset": offset}
        if filter:
            params["filter"] = str(filter)
            
        data = self.client.get(self.path, params=params)
        adapter = TypeAdapter(ListResponse[self.model])
        return adapter.validate_python(data)

    def iter_all(self, filter: str | Filter | None = None, chunk_size: int = 1000) -> Generator[T, None, None]:
        offset = 0
        while True:
            response = self.list(limit=chunk_size, offset=offset, filter=filter)
            for row in response.rows:
                yield row
            if len(response.rows) < chunk_size:
                break
            offset += chunk_size

class AsyncStockReportAPI:
    def __init__(self, client):
        self.all = AsyncReportEndpoint[StockRow](client, "report/stock/all", StockRow)
        self.bystore = AsyncReportEndpoint[StockRow](client, "report/stock/bystore", StockRow)

class SyncStockReportAPI:
    def __init__(self, client):
        self.all = SyncReportEndpoint[StockRow](client, "report/stock/all", StockRow)
        self.bystore = SyncReportEndpoint[StockRow](client, "report/stock/bystore", StockRow)

class AsyncReportAPI:
    def __init__(self, client):
        self.stock = AsyncStockReportAPI(client)
        self.sales = AsyncReportEndpoint[SalesRow](client, "report/sales/plotseries", SalesRow) # default simple sales endpoint

class SyncReportAPI:
    def __init__(self, client):
        self.stock = SyncStockReportAPI(client)
        self.sales = SyncReportEndpoint[SalesRow](client, "report/sales/plotseries", SalesRow)
