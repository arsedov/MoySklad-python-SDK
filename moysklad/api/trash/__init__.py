from moysklad.api.base import AsyncEndpoint, SyncEndpoint
from moysklad.models.trash.item import TrashItem

class AsyncTrashAPI:
    def __init__(self, client):
        self.client = client
        self.item = AsyncEndpoint[TrashItem](client, "trash", TrashItem)
        
    async def restore(self, uuid: str) -> None:
        await self.client.post(f"trash/{uuid}/restore")

class SyncTrashAPI:
    def __init__(self, client):
        self.client = client
        self.item = SyncEndpoint[TrashItem](client, "trash", TrashItem)
        
    def restore(self, uuid: str) -> None:
        self.client.post(f"trash/{uuid}/restore")
