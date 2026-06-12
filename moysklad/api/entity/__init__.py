from typing import Any, TypeVar, Generic, Type
from pydantic import BaseModel
from moysklad.models.base import ListResponse

T = TypeVar("T", bound=BaseModel)

class AsyncEndpoint(Generic[T]):
    def __init__(self, client: Any, path: str, model: Type[T]):
        self.client = client
        self.path = path
        self.model = model

    async def get(self, uuid: str, expand: str | None = None) -> T:
        params = {}
        if expand:
            params["expand"] = expand
        data = await self.client.get(f"{self.path}/{uuid}", params=params)
        return self.model.model_validate(data)

    async def list(self, limit: int = 1000, offset: int = 0, expand: str | None = None) -> ListResponse[T]:
        params = {"limit": limit, "offset": offset}
        if expand:
            params["expand"] = expand
        data = await self.client.get(self.path, params=params)
        
        # Pydantic currently doesn't directly parse Generic types from dict easily without a little trick,
        # but ListResponse[self.model] works in pydantic v2 via TypeAdapter or just direct validation
        from pydantic import TypeAdapter
        adapter = TypeAdapter(ListResponse[self.model])
        return adapter.validate_python(data)

    async def create(self, data: dict[str, Any] | BaseModel) -> T:
        payload = data.model_dump(exclude_unset=True) if isinstance(data, BaseModel) else data
        response_data = await self.client.post(self.path, json=payload)
        return self.model.model_validate(response_data)

class SyncEndpoint(Generic[T]):
    def __init__(self, client: Any, path: str, model: Type[T]):
        self.client = client
        self.path = path
        self.model = model

    def get(self, uuid: str, expand: str | None = None) -> T:
        params = {}
        if expand:
            params["expand"] = expand
        data = self.client.get(f"{self.path}/{uuid}", params=params)
        return self.model.model_validate(data)

    def list(self, limit: int = 1000, offset: int = 0, expand: str | None = None) -> ListResponse[T]:
        params = {"limit": limit, "offset": offset}
        if expand:
            params["expand"] = expand
        data = self.client.get(self.path, params=params)
        
        from pydantic import TypeAdapter
        adapter = TypeAdapter(ListResponse[self.model])
        return adapter.validate_python(data)

    def create(self, data: dict[str, Any] | BaseModel) -> T:
        payload = data.model_dump(exclude_unset=True) if isinstance(data, BaseModel) else data
        response_data = self.client.post(self.path, json=payload)
        return self.model.model_validate(response_data)


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
