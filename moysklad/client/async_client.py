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
        from moysklad.api.bonus_program import AsyncBonusProgramAPI
        from moysklad.api.webhook import AsyncWebhookAPI
        from moysklad.api.retail import AsyncRetailAPI
        from moysklad.api.report import AsyncReportAPI
        self.entity = AsyncEntityAPI(self)
        self.document = AsyncDocumentAPI(self)
        self.bonus_program = AsyncBonusProgramAPI(self)
        self.webhook = AsyncWebhookAPI(self)
        self.retail = AsyncRetailAPI(self)
        self.report = AsyncReportAPI(self)

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
