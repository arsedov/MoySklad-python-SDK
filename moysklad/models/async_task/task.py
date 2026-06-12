from pydantic import BaseModel
from moysklad.models.base import Meta

class AsyncTask(BaseModel):
    meta: Meta
    id: str
    accountId: str
    state: str
    request: str
    resultUrl: str | None = None
    errors: list[dict] | None = None
