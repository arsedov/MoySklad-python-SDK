import base64
from typing import Any
import httpx
from moysklad.client.exceptions import AuthError, RateLimitError, APIError

class BaseClient:
    BASE_URL = "https://api.moysklad.ru/api/remap/1.2"

    def __init__(self, token: str | None = None, login: str | None = None, password: str | None = None):
        self.headers = {
            "Accept-Encoding": "gzip",
            "Content-Type": "application/json"
        }
        if token:
            self.headers["Authorization"] = f"Bearer {token}"
        elif login and password:
            credentials = f"{login}:{password}"
            encoded = base64.b64encode(credentials.encode()).decode("utf-8")
            self.headers["Authorization"] = f"Basic {encoded}"
        else:
            raise ValueError("Provide either 'token' or 'login' and 'password'")

    def _handle_response(self, response: httpx.Response) -> dict[str, Any]:
        if response.status_code == 200 or response.status_code == 201:
            if response.content:
                return response.json()
            return {}
        
        if response.status_code == 401:
            raise AuthError("Invalid credentials")
        if response.status_code == 429:
            raise RateLimitError("Too many requests to Moysklad API")
            
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
            
        raise APIError(
            message=f"Moysklad API Error: {response.status_code}",
            status_code=response.status_code,
            details=data
        )

    def _build_url(self, path: str) -> str:
        path = path.lstrip("/")
        return f"{self.BASE_URL}/{path}"
