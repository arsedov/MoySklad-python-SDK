import time
from typing import Any
import httpx
from moysklad.client.base import BaseClient

class MoyskladClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._client = httpx.Client(headers=self.headers, timeout=self.timeout)

        # Initialize API groups
        from moysklad.api.entity import SyncEntityAPI
        from moysklad.api.document import SyncDocumentAPI
        from moysklad.api.bonus_program import SyncBonusProgramAPI
        from moysklad.api.webhook import SyncWebhookAPI
        from moysklad.api.retail import SyncRetailAPI
        from moysklad.api.report import SyncReportAPI
        from moysklad.api.audit import SyncAuditAPI
        from moysklad.api.async_task import SyncAsyncTaskAPI
        from moysklad.api.context import SyncContextAPI
        from moysklad.api.trash import SyncTrashAPI

        self.entity = SyncEntityAPI(self)
        self.document = SyncDocumentAPI(self)
        self.bonus_program = SyncBonusProgramAPI(self)
        self.webhook = SyncWebhookAPI(self)
        self.retail = SyncRetailAPI(self)
        self.report = SyncReportAPI(self)
        self.audit = SyncAuditAPI(self)
        self.async_task = SyncAsyncTaskAPI(self)
        self.context = SyncContextAPI(self)
        self.trash = SyncTrashAPI(self)

    def _request(self, method: str, path: str, **kwargs: Any) -> dict[str, Any]:
        url = self._build_url(path)
        for attempt in range(self.max_retries + 1):
            response = self._client.request(method, url, **kwargs)
            if response.status_code == 429 and attempt < self.max_retries:
                time.sleep(self._retry_delay(response, attempt))
                continue
            return self._handle_response(response)
        return self._handle_response(response)

    def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        return self._request("GET", path, params=params)

    def post(self, path: str, json: Any | None = None) -> dict[str, Any]:
        return self._request("POST", path, json=json)

    def put(self, path: str, json: Any | None = None) -> dict[str, Any]:
        return self._request("PUT", path, json=json)

    def delete(self, path: str, json: Any | None = None) -> dict[str, Any]:
        return self._request("DELETE", path, json=json)

    def close(self):
        self._client.close()

    def __enter__(self) -> "MoyskladClient":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()
