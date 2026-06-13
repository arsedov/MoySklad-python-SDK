from typing import Any, TypeVar, Generic, Type, AsyncGenerator, Generator
from pydantic import BaseModel
from moysklad.models.base import ListResponse
from moysklad.utils.filters import Filter

T = TypeVar("T", bound=BaseModel)

class AsyncEndpoint(Generic[T]):
    def __init__(self, client: Any, path: str, model: Type[T]):
        self.client = client
        self.path = path
        self.model = model

    async def metadata(self) -> dict[str, Any]:
        return await self.client.get(f"{self.path}/metadata")

    async def export(self, uuid: str, template: dict[str, Any]) -> dict[str, Any]:
        return await self.client.post(f"{self.path}/{uuid}/export", json={"template": template})

    async def images(self, uuid: str) -> dict[str, Any]:
        return await self.client.get(f"{self.path}/{uuid}/images")

    async def get(self, uuid: str, expand: str | None = None) -> T:
        params = {}
        if expand:
            params["expand"] = expand
        data = await self.client.get(f"{self.path}/{uuid}", params=params)
        return self.model.model_validate(data)

    async def list(self, limit: int = 1000, offset: int = 0, expand: str | None = None, filter: str | Filter | None = None) -> ListResponse[T]:
        params = {"limit": limit, "offset": offset}
        if expand:
            params["expand"] = expand
        if filter:
            params["filter"] = str(filter)
            
        data = await self.client.get(self.path, params=params)
        
        from pydantic import TypeAdapter
        adapter = TypeAdapter(ListResponse[self.model])
        return adapter.validate_python(data)

    async def iter_all(self, expand: str | None = None, filter: str | Filter | None = None, chunk_size: int = 1000) -> AsyncGenerator[T, None]:
        offset = 0
        while True:
            response = await self.list(limit=chunk_size, offset=offset, expand=expand, filter=filter)
            for row in response.rows:
                yield row
            
            offset += chunk_size
            # The moysklad api returns 'size' which is total available
            # However, sometimes it's simpler to break if we received less rows than limit
            if len(response.rows) < chunk_size:
                break

    async def create(self, data: dict[str, Any] | BaseModel) -> T:
        payload = data.model_dump(exclude_unset=True) if isinstance(data, BaseModel) else data
        response_data = await self.client.post(self.path, json=payload)
        return self.model.model_validate(response_data)

class SyncEndpoint(Generic[T]):
    def __init__(self, client: Any, path: str, model: Type[T]):
        self.client = client
        self.path = path
        self.model = model

    def metadata(self) -> dict[str, Any]:
        return self.client.get(f"{self.path}/metadata")

    def export(self, uuid: str, template: dict[str, Any]) -> dict[str, Any]:
        return self.client.post(f"{self.path}/{uuid}/export", json={"template": template})

    def images(self, uuid: str) -> dict[str, Any]:
        return self.client.get(f"{self.path}/{uuid}/images")

    def get(self, uuid: str, expand: str | None = None) -> T:
        params = {}
        if expand:
            params["expand"] = expand
        data = self.client.get(f"{self.path}/{uuid}", params=params)
        return self.model.model_validate(data)

    def list(self, limit: int = 1000, offset: int = 0, expand: str | None = None, filter: str | Filter | None = None) -> ListResponse[T]:
        params = {"limit": limit, "offset": offset}
        if expand:
            params["expand"] = expand
        if filter:
            params["filter"] = str(filter)

        data = self.client.get(self.path, params=params)
        
        from pydantic import TypeAdapter
        adapter = TypeAdapter(ListResponse[self.model])
        return adapter.validate_python(data)

    def iter_all(self, expand: str | None = None, filter: str | Filter | None = None, chunk_size: int = 1000) -> Generator[T, None, None]:
        offset = 0
        while True:
            response = self.list(limit=chunk_size, offset=offset, expand=expand, filter=filter)
            for row in response.rows:
                yield row
            
            offset += chunk_size
            if len(response.rows) < chunk_size:
                break

    def create(self, data: dict[str, Any] | BaseModel) -> T:
        payload = data.model_dump(exclude_unset=True) if isinstance(data, BaseModel) else data
        response_data = self.client.post(self.path, json=payload)
        return self.model.model_validate(response_data)
