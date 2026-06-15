import pytest
import respx
import httpx
from moysklad import AsyncMoyskladClient


def _product(uuid: str, name: str) -> dict:
    return {
        "meta": {
            "href": f"https://api.moysklad.ru/api/remap/1.2/entity/product/{uuid}",
            "type": "product",
            "mediaType": "application/json",
        },
        "id": uuid,
        "accountId": "acc",
        "name": name,
        "updated": "2023-01-01 12:00:00",
        "externalCode": "EXT",
    }


@pytest.fixture
def client():
    return AsyncMoyskladClient(token="t")


@pytest.mark.asyncio
@respx.mock
async def test_update(client):
    uuid = "abc"
    route = respx.put(f"https://api.moysklad.ru/api/remap/1.2/entity/product/{uuid}").mock(
        return_value=httpx.Response(200, json=_product(uuid, "Renamed"))
    )
    result = await client.entity.product.update(uuid, {"name": "Renamed"})
    assert result.name == "Renamed"
    assert route.called
    assert respx.calls.last.request.method == "PUT"


@pytest.mark.asyncio
@respx.mock
async def test_delete(client):
    uuid = "abc"
    route = respx.delete(f"https://api.moysklad.ru/api/remap/1.2/entity/product/{uuid}").mock(
        return_value=httpx.Response(200)
    )
    result = await client.entity.product.delete(uuid)
    assert result is None
    assert route.called


@pytest.mark.asyncio
@respx.mock
async def test_delete_204_no_content(client):
    uuid = "abc"
    respx.delete(f"https://api.moysklad.ru/api/remap/1.2/entity/product/{uuid}").mock(
        return_value=httpx.Response(204)
    )
    # 204 не должен падать на разборе JSON.
    assert await client.entity.product.delete(uuid) is None


@pytest.mark.asyncio
@respx.mock
async def test_create_bulk(client):
    route = respx.post("https://api.moysklad.ru/api/remap/1.2/entity/product").mock(
        return_value=httpx.Response(200, json=[_product("1", "A"), _product("2", "B")])
    )
    result = await client.entity.product.create_bulk([{"name": "A"}, {"name": "B"}])
    assert [p.name for p in result] == ["A", "B"]
    assert route.called


@pytest.mark.asyncio
@respx.mock
async def test_delete_bulk_builds_meta(client):
    route = respx.post("https://api.moysklad.ru/api/remap/1.2/entity/product/delete").mock(
        return_value=httpx.Response(200, json=[{"info": "ok"}])
    )
    await client.entity.product.delete_bulk(["id-1", "id-2"])
    import json
    sent = json.loads(respx.calls.last.request.content)
    assert sent[0]["meta"]["href"].endswith("/entity/product/id-1")
    assert sent[0]["meta"]["type"] == "product"
    assert route.called
