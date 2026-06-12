import pytest
import respx
import httpx
from moysklad import AsyncMoyskladClient

@pytest.fixture
def async_client():
    return AsyncMoyskladClient(token="test_token")

@pytest.mark.asyncio
@respx.mock
async def test_get_product(async_client):
    product_uuid = "12345-abcde"
    mock_response = {
        "meta": {
            "href": f"https://api.moysklad.ru/api/remap/1.2/entity/product/{product_uuid}",
            "type": "product",
            "mediaType": "application/json"
        },
        "id": product_uuid,
        "accountId": "account123",
        "name": "Test Product",
        "updated": "2023-01-01 12:00:00",
        "externalCode": "EXT-1"
    }

    respx.get(f"https://api.moysklad.ru/api/remap/1.2/entity/product/{product_uuid}").mock(
        return_value=httpx.Response(200, json=mock_response)
    )

    product = await async_client.entity.product.get(product_uuid)
    
    assert product.id == product_uuid
    assert product.name == "Test Product"
    assert product.externalCode == "EXT-1"

@pytest.mark.asyncio
@respx.mock
async def test_list_products(async_client):
    mock_response = {
        "context": {
            "employee": {
                "meta": {
                    "href": "https://api.moysklad.ru/api/remap/1.2/context/employee/1",
                    "type": "employee",
                    "mediaType": "application/json"
                }
            }
        },
        "meta": {
            "href": "https://api.moysklad.ru/api/remap/1.2/entity/product",
            "type": "product",
            "mediaType": "application/json",
            "size": 1,
            "limit": 1000,
            "offset": 0
        },
        "rows": [
            {
                "meta": {
                    "href": "https://api.moysklad.ru/api/remap/1.2/entity/product/1",
                    "type": "product",
                    "mediaType": "application/json"
                },
                "id": "1",
                "accountId": "account123",
                "name": "Test Product 1",
                "updated": "2023-01-01 12:00:00",
                "externalCode": "EXT-1"
            }
        ]
    }

    respx.get("https://api.moysklad.ru/api/remap/1.2/entity/product").mock(
        return_value=httpx.Response(200, json=mock_response)
    )

    response = await async_client.entity.product.list()
    
    assert len(response.rows) == 1
    assert response.rows[0].name == "Test Product 1"
