import pytest
import respx
import httpx
from moysklad import AsyncMoyskladClient, RateLimitError

@pytest.mark.asyncio
@respx.mock
async def test_rate_limit_error():
    client = AsyncMoyskladClient(token="test_token")
    
    respx.get("https://api.moysklad.ru/api/remap/1.2/entity/product").mock(
        return_value=httpx.Response(429, json={"errors": [{"error": "Too Many Requests"}]})
    )

    with pytest.raises(RateLimitError):
        await client.entity.product.list()
