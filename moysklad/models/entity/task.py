from moysklad.models.base import BaseEntity

class Task(BaseEntity):
    description: str | None = None
    assignee: dict | None = None
    done: bool = False
    dueToDate: str | None = None
