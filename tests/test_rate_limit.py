import pytest
import respx
import httpx
from moysklad import AsyncMoyskladClient, RateLimitError

@pytest.mark.asyncio
@respx.mock
async def test_rate_limit_error_after_retries():
    # max_retries=0 — без ожиданий, ошибка сразу.
    client = AsyncMoyskladClient(token="test_token", max_retries=0)

    respx.get("https://api.moysklad.ru/api/remap/1.2/entity/product").mock(
        return_value=httpx.Response(429, json={"errors": [{"error": "Too Many Requests"}]})
    )

    with pytest.raises(RateLimitError):
        await client.entity.product.list()


@pytest.mark.asyncio
@respx.mock
async def test_rate_limit_retry_then_success():
    # Первый ответ 429 с коротким Retry-After, второй — успех.
    client = AsyncMoyskladClient(token="test_token", max_retries=3)

    page = {
        "context": {"employee": {"meta": {"href": "", "type": "employee", "mediaType": "application/json"}}},
        "meta": {"href": "", "type": "product", "mediaType": "application/json", "size": 0},
        "rows": [],
    }

    route = respx.get("https://api.moysklad.ru/api/remap/1.2/entity/product")
    route.side_effect = [
        httpx.Response(429, headers={"X-RateLimit-Retry-After": "1"}),  # 1 мс
        httpx.Response(200, json=page),
    ]

    result = await client.entity.product.list()
    assert result.rows == []
    assert route.call_count == 2
