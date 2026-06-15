from __future__ import annotations
from typing import Any, TypeVar, Generic, Type, AsyncGenerator, Generator, List
from pydantic import BaseModel, TypeAdapter
from moysklad.models.base import ListResponse
from moysklad.utils.filters import Filter

T = TypeVar("T", bound=BaseModel)


def _dump(data: dict[str, Any] | BaseModel) -> dict[str, Any]:
    return data.model_dump(exclude_unset=True, by_alias=True) if isinstance(data, BaseModel) else data


class AsyncEndpoint(Generic[T]):
    def __init__(self, client: Any, path: str, model: Type[T]):
        self.client = client
        self.path = path
        self.model = model

    def _list_adapter(self) -> TypeAdapter:
        return TypeAdapter(ListResponse[self.model])

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
        params: dict[str, Any] = {"limit": limit, "offset": offset}
        if expand:
            params["expand"] = expand
        if filter:
            params["filter"] = str(filter)

        data = await self.client.get(self.path, params=params)
        return self._list_adapter().validate_python(data)

    async def iter_all(self, expand: str | None = None, filter: str | Filter | None = None, chunk_size: int = 1000) -> AsyncGenerator[T, None]:
        # МойСклад ограничивает limit максимумом в 1000.
        chunk_size = min(chunk_size, 1000)
        offset = 0
        while True:
            response = await self.list(limit=chunk_size, offset=offset, expand=expand, filter=filter)
            for row in response.rows:
                yield row

            offset += len(response.rows)
            # Останавливаемся, когда забрали все записи (meta.size) или
            # сервер вернул пустую страницу.
            if not response.rows or (response.meta.size is not None and offset >= response.meta.size):
                break

    async def create(self, data: dict[str, Any] | BaseModel) -> T:
        response_data = await self.client.post(self.path, json=_dump(data))
        return self.model.model_validate(response_data)

    async def update(self, uuid: str, data: dict[str, Any] | BaseModel) -> T:
        response_data = await self.client.put(f"{self.path}/{uuid}", json=_dump(data))
        return self.model.model_validate(response_data)

    async def delete(self, uuid: str) -> None:
        await self.client.delete(f"{self.path}/{uuid}")

    async def create_bulk(self, items: List[dict[str, Any] | BaseModel]) -> List[T]:
        """Массовое создание/обновление (POST со списком). Элементы с `meta`
        обновляются, без `meta` — создаются."""
        payload = [_dump(item) for item in items]
        response_data = await self.client.post(self.path, json=payload)
        return [self.model.model_validate(row) for row in response_data]

    async def delete_bulk(self, items: List[dict[str, Any] | str]) -> dict[str, Any]:
        """Массовое удаление. Принимает список meta-объектов или uuid."""
        payload = [_meta_ref(self.path, item) for item in items]
        return await self.client.post(f"{self.path}/delete", json=payload)


class SyncEndpoint(Generic[T]):
    def __init__(self, client: Any, path: str, model: Type[T]):
        self.client = client
        self.path = path
        self.model = model

    def _list_adapter(self) -> TypeAdapter:
        return TypeAdapter(ListResponse[self.model])

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
        params: dict[str, Any] = {"limit": limit, "offset": offset}
        if expand:
            params["expand"] = expand
        if filter:
            params["filter"] = str(filter)

        data = self.client.get(self.path, params=params)
        return self._list_adapter().validate_python(data)

    def iter_all(self, expand: str | None = None, filter: str | Filter | None = None, chunk_size: int = 1000) -> Generator[T, None, None]:
        chunk_size = min(chunk_size, 1000)
        offset = 0
        while True:
            response = self.list(limit=chunk_size, offset=offset, expand=expand, filter=filter)
            for row in response.rows:
                yield row

            offset += len(response.rows)
            if not response.rows or (response.meta.size is not None and offset >= response.meta.size):
                break

    def create(self, data: dict[str, Any] | BaseModel) -> T:
        response_data = self.client.post(self.path, json=_dump(data))
        return self.model.model_validate(response_data)

    def update(self, uuid: str, data: dict[str, Any] | BaseModel) -> T:
        response_data = self.client.put(f"{self.path}/{uuid}", json=_dump(data))
        return self.model.model_validate(response_data)

    def delete(self, uuid: str) -> None:
        self.client.delete(f"{self.path}/{uuid}")

    def create_bulk(self, items: List[dict[str, Any] | BaseModel]) -> List[T]:
        payload = [_dump(item) for item in items]
        response_data = self.client.post(self.path, json=payload)
        return [self.model.model_validate(row) for row in response_data]

    def delete_bulk(self, items: List[dict[str, Any] | str]) -> dict[str, Any]:
        payload = [_meta_ref(self.path, item) for item in items]
        return self.client.post(f"{self.path}/delete", json=payload)


def _meta_ref(path: str, item: dict[str, Any] | str) -> dict[str, Any]:
    """Строит {"meta": {...}} для массового удаления из uuid или готового объекта."""
    if isinstance(item, str):
        href = f"https://api.moysklad.ru/api/remap/1.2/{path}/{item}"
        entity_type = path.split("/")[-1]
        return {"meta": {"href": href, "type": entity_type, "mediaType": "application/json"}}
    if "meta" in item:
        return {"meta": item["meta"]}
    return item
