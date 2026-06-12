from moysklad.api.base import AsyncEndpoint, SyncEndpoint
from moysklad.models.audit.event import AuditEvent

class AsyncAuditAPI:
    def __init__(self, client):
        self.event = AsyncEndpoint[AuditEvent](client, "audit", AuditEvent)

class SyncAuditAPI:
    def __init__(self, client):
        self.event = SyncEndpoint[AuditEvent](client, "audit", AuditEvent)
