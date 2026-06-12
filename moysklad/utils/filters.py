from typing import Any

class Filter:
    """Билдер для фильтров МойСклад.
    Например: Filter().eq("name", "Товар 1").gt("sum", 100).build() -> "name=Товар 1;sum>100"
    """
    def __init__(self):
        self._conditions = []

    def _add(self, field: str, operator: str, value: Any) -> "Filter":
        if isinstance(value, bool):
            value_str = "true" if value else "false"
        else:
            value_str = str(value)
        self._conditions.append(f"{field}{operator}{value_str}")
        return self

    def eq(self, field: str, value: Any) -> "Filter":
        return self._add(field, "=", value)

    def neq(self, field: str, value: Any) -> "Filter":
        return self._add(field, "!=", value)

    def gt(self, field: str, value: Any) -> "Filter":
        return self._add(field, ">", value)

    def lt(self, field: str, value: Any) -> "Filter":
        return self._add(field, "<", value)

    def gte(self, field: str, value: Any) -> "Filter":
        return self._add(field, ">=", value)

    def lte(self, field: str, value: Any) -> "Filter":
        return self._add(field, "<=", value)

    def contains(self, field: str, value: Any) -> "Filter":
        return self._add(field, "~", value)

    def build(self) -> str:
        return ";".join(self._conditions)

    def __str__(self) -> str:
        return self.build()
