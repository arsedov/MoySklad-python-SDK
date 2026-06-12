from typing import Any
import httpx
from moysklad.client.base import BaseClient

class MoyskladClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._client = httpx.Client(headers=self.headers)
        
        # Initialize API groups
        from moysklad.api.entity import SyncEntityAPI
        self.entity = SyncEntityAPI(self)

    def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        url = self._build_url(path)
        response = self._client.get(url, params=params)
        return self._handle_response(response)

    def post(self, path: str, json: dict[str, Any] | None = None) -> dict[str, Any]:
        url = self._build_url(path)
        response = self._client.post(url, json=json)
        return self._handle_response(response)

    def put(self, path: str, json: dict[str, Any] | None = None) -> dict[str, Any]:
        url = self._build_url(path)
        response = self._client.put(url, json=json)
        return self._handle_response(response)

    def delete(self, path: str) -> dict[str, Any]:
        url = self._build_url(path)
        response = self._client.delete(url)
        return self._handle_response(response)

    def close(self):
        self._client.close()
