from moysklad.models.context.models import CompanySettings, ContextEmployee
from pydantic import TypeAdapter

class AsyncContextAPI:
    def __init__(self, client):
        self.client = client

    async def companysettings(self) -> CompanySettings:
        data = await self.client.get("context/companysettings")
        adapter = TypeAdapter(CompanySettings)
        return adapter.validate_python(data)

    async def employee(self) -> ContextEmployee:
        data = await self.client.get("context/employee")
        adapter = TypeAdapter(ContextEmployee)
        return adapter.validate_python(data)

class SyncContextAPI:
    def __init__(self, client):
        self.client = client

    def companysettings(self) -> CompanySettings:
        data = self.client.get("context/companysettings")
        adapter = TypeAdapter(CompanySettings)
        return adapter.validate_python(data)

    def employee(self) -> ContextEmployee:
        data = self.client.get("context/employee")
        adapter = TypeAdapter(ContextEmployee)
        return adapter.validate_python(data)
