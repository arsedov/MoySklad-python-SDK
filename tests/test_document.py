import pytest
import respx
import httpx
from moysklad import AsyncMoyskladClient

@pytest.fixture
def async_client():
    return AsyncMoyskladClient(token="test_token")

@pytest.mark.asyncio
@respx.mock
async def test_create_customer_order(async_client):
    mock_response = {
        "meta": {
            "href": "https://api.moysklad.ru/api/remap/1.2/entity/customerorder/123",
            "type": "customerorder",
            "mediaType": "application/json"
        },
        "id": "123",
        "accountId": "account123",
        "name": "Order 001",
        "moment": "2023-01-01 12:00:00",
        "applicable": True,
        "sum": 1000.0,
        "updated": "2023-01-01 12:00:00",
        "agent": {"meta": {"href": "...", "type": "counterparty", "mediaType": "application/json"}},
        "organization": {"meta": {"href": "...", "type": "organization", "mediaType": "application/json"}}
    }

    respx.post("https://api.moysklad.ru/api/remap/1.2/entity/customerorder").mock(
        return_value=httpx.Response(200, json=mock_response)
    )

    data = {
        "organization": {"meta": {"href": "...", "type": "organization", "mediaType": "application/json"}},
        "agent": {"meta": {"href": "...", "type": "counterparty", "mediaType": "application/json"}}
    }
    
    order = await async_client.document.customerorder.create(data)
    
    assert order.id == "123"
    assert order.name == "Order 001"
    assert order.sum == 1000.0
