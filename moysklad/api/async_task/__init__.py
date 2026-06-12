from moysklad.api.base import AsyncEndpoint, SyncEndpoint
from moysklad.models.async_task.task import AsyncTask

class AsyncAsyncTaskAPI:
    def __init__(self, client):
        self.task = AsyncEndpoint[AsyncTask](client, "async/task", AsyncTask)

class SyncAsyncTaskAPI:
    def __init__(self, client):
        self.task = SyncEndpoint[AsyncTask](client, "async/task", AsyncTask)
