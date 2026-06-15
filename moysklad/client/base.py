import base64
from typing import Any
import httpx
from moysklad.client.exceptions import AuthError, RateLimitError, APIError

# Значение по умолчанию для таймаута httpx (сек). Длинные отчёты/экспорт
# не должны падать на дефолтных 5с httpx.
DEFAULT_TIMEOUT = 30.0
DEFAULT_MAX_RETRIES = 3


class BaseClient:
    BASE_URL = "https://api.moysklad.ru/api/remap/1.2"

    def __init__(
        self,
        token: str | None = None,
        login: str | None = None,
        password: str | None = None,
        timeout: float | httpx.Timeout = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ):
        self.timeout = timeout
        self.max_retries = max_retries
        self.headers = {
            "Accept-Encoding": "gzip",
            "Content-Type": "application/json",
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
        # 200 OK, 201 Created, 204 No Content (например, после DELETE).
        if response.status_code in (200, 201, 204):
            if response.status_code == 204 or not response.content:
                return {}
            return response.json()

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
            details=data,
        )

    def _retry_delay(self, response: httpx.Response, attempt: int) -> float:
        """Сколько ждать перед повтором запроса при 429.

        МойСклад присылает `X-RateLimit-Retry-After` в миллисекундах. Также
        поддерживаем стандартный заголовок `Retry-After` (секунды). Если
        заголовков нет — экспоненциальный backoff.
        """
        ms = response.headers.get("X-RateLimit-Retry-After")
        if ms:
            try:
                return max(0.0, float(ms) / 1000.0)
            except ValueError:
                pass
        retry_after = response.headers.get("Retry-After")
        if retry_after:
            try:
                return max(0.0, float(retry_after))
            except ValueError:
                pass
        return float(2 ** attempt)

    def _build_url(self, path: str) -> str:
        path = path.lstrip("/")
        return f"{self.BASE_URL}/{path}"
