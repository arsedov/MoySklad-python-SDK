from moysklad.api.base import AsyncEndpoint, SyncEndpoint
from moysklad.models.webhook.webhook import Webhook

class AsyncWebhookAPI:
    def __init__(self, client):
        self.webhook = AsyncEndpoint[Webhook](client, "entity/webhook", Webhook)

class SyncWebhookAPI:
    def __init__(self, client):
        self.webhook = SyncEndpoint[Webhook](client, "entity/webhook", Webhook)
