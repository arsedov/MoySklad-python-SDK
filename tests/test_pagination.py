import pytest
import respx
import httpx
from moysklad import AsyncMoyskladClient

@pytest.mark.asyncio
@respx.mock
async def test_iter_all():
    client = AsyncMoyskladClient(token="test")
    
    # Mocking two pages
    page1 = {
        "context": {"employee": {"meta": {"href": "", "type": "employee", "mediaType": "application/json"}}},
        "meta": {"href": "", "type": "product", "mediaType": "application/json", "size": 2, "limit": 1, "offset": 0},
        "rows": [{"meta": {"href": "", "type": "product", "mediaType": "application/json"}, "id": "1", "accountId": "acc", "name": "Prod 1", "externalCode": "1", "updated": "2023"}]
    }
    
    page2 = {
        "context": {"employee": {"meta": {"href": "", "type": "employee", "mediaType": "application/json"}}},
        "meta": {"href": "", "type": "product", "mediaType": "application/json", "size": 2, "limit": 1, "offset": 1},
        "rows": [{"meta": {"href": "", "type": "product", "mediaType": "application/json"}, "id": "2", "accountId": "acc", "name": "Prod 2", "externalCode": "2", "updated": "2023"}]
    }
    
    page3 = {
        "context": {"employee": {"meta": {"href": "", "type": "employee", "mediaType": "application/json"}}},
        "meta": {"href": "", "type": "product", "mediaType": "application/json", "size": 2, "limit": 1, "offset": 2},
        "rows": []
    }

    respx.get("https://api.moysklad.ru/api/remap/1.2/entity/product?limit=1&offset=0").mock(
        return_value=httpx.Response(200, json=page1)
    )
    respx.get("https://api.moysklad.ru/api/remap/1.2/entity/product?limit=1&offset=1").mock(
        return_value=httpx.Response(200, json=page2)
    )
    respx.get("https://api.moysklad.ru/api/remap/1.2/entity/product?limit=1&offset=2").mock(
        return_value=httpx.Response(200, json=page3)
    )

    items = []
    async for item in client.entity.product.iter_all(chunk_size=1):
        items.append(item)
        
    assert len(items) == 2
    assert items[0].name == "Prod 1"
    assert items[1].name == "Prod 2"
