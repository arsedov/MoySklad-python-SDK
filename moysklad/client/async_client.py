from typing import Any
import httpx
from moysklad.client.base import BaseClient

class AsyncMoyskladClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._client = httpx.AsyncClient(headers=self.headers)
        
        # Initialize API groups
        from moysklad.api.entity import AsyncEntityAPI
        from moysklad.api.document import AsyncDocumentAPI
        self.entity = AsyncEntityAPI(self)
        self.document = AsyncDocumentAPI(self)

    async def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        url = self._build_url(path)
        response = await self._client.get(url, params=params)
        return self._handle_response(response)

    async def post(self, path: str, json: dict[str, Any] | None = None) -> dict[str, Any]:
        url = self._build_url(path)
        response = await self._client.post(url, json=json)
        return self._handle_response(response)

    async def put(self, path: str, json: dict[str, Any] | None = None) -> dict[str, Any]:
        url = self._build_url(path)
        response = await self._client.put(url, json=json)
        return self._handle_response(response)

    async def delete(self, path: str) -> dict[str, Any]:
        url = self._build_url(path)
        response = await self._client.delete(url)
        return self._handle_response(response)

    async def close(self):
        await self._client.aclose()
