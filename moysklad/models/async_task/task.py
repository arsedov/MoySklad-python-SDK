from pydantic import BaseModel
from moysklad.models.base import Meta

class AsyncTask(BaseModel):
    meta: Meta
    id: str | None = None
    accountId: str | None = None
    state: str | None = None
    request: str | None = None
    resultUrl: str | None = None
    errors: list[dict] | None = None
