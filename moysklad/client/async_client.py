import asyncio
from typing import Any
import httpx
from moysklad.client.base import BaseClient

class AsyncMoyskladClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._client = httpx.AsyncClient(headers=self.headers, timeout=self.timeout)

        # Initialize API groups
        from moysklad.api.entity import AsyncEntityAPI
        from moysklad.api.document import AsyncDocumentAPI
        from moysklad.api.bonus_program import AsyncBonusProgramAPI
        from moysklad.api.webhook import AsyncWebhookAPI
        from moysklad.api.retail import AsyncRetailAPI
        from moysklad.api.report import AsyncReportAPI
        from moysklad.api.audit import AsyncAuditAPI
        from moysklad.api.async_task import AsyncAsyncTaskAPI
        from moysklad.api.context import AsyncContextAPI
        from moysklad.api.trash import AsyncTrashAPI

        self.entity = AsyncEntityAPI(self)
        self.document = AsyncDocumentAPI(self)
        self.bonus_program = AsyncBonusProgramAPI(self)
        self.webhook = AsyncWebhookAPI(self)
        self.retail = AsyncRetailAPI(self)
        self.report = AsyncReportAPI(self)
        self.audit = AsyncAuditAPI(self)
        self.async_task = AsyncAsyncTaskAPI(self)
        self.context = AsyncContextAPI(self)
        self.trash = AsyncTrashAPI(self)

    async def _request(self, method: str, path: str, **kwargs: Any) -> dict[str, Any]:
        url = self._build_url(path)
        for attempt in range(self.max_retries + 1):
            response = await self._client.request(method, url, **kwargs)
            if response.status_code == 429 and attempt < self.max_retries:
                await asyncio.sleep(self._retry_delay(response, attempt))
                continue
            return self._handle_response(response)
        return self._handle_response(response)

    async def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        return await self._request("GET", path, params=params)

    async def post(self, path: str, json: Any | None = None) -> dict[str, Any]:
        return await self._request("POST", path, json=json)

    async def put(self, path: str, json: Any | None = None) -> dict[str, Any]:
        return await self._request("PUT", path, json=json)

    async def delete(self, path: str, json: Any | None = None) -> dict[str, Any]:
        return await self._request("DELETE", path, json=json)

    async def close(self):
        await self._client.aclose()

    async def __aenter__(self) -> "AsyncMoyskladClient":
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self.close()
