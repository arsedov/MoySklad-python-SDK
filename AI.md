# Руководство для ИИ-разработчиков (AI & LLM Guide)

Этот файл содержит структурное описание кодовой базы `moysklad-python`, архитектурные паттерны, правила расширения функционала и рекомендации для ИИ-агентов, которые будут работать с данным репозиторием.

---

## 📌 Архитектура проекта

Кодовая база представляет собой асинхронный и синхронный SDK для работы с JSON API МойСклад 1.2.

### Основные компоненты и их связи:

1. **Базовый клиент (`BaseClient`)**:
   - Расположение: [moysklad/client/base.py](moysklad/client/base.py)
   - Функционал: Настройка авторизации (Bearer Token или Basic Auth), формирование URL (`BASE_URL = https://api.moysklad.ru/api/remap/1.2`), обработка ошибок в методе `_handle_response`.
2. **Асинхронный клиент (`AsyncMoyskladClient`)**:
   - Расположение: [moysklad/client/async_client.py](moysklad/client/async_client.py)
   - Функционал: Использует `httpx.AsyncClient` для выполнения неблокирующих сетевых запросов. Инициализирует асинхронные группы API (например, `self.entity`, `self.document`, `self.retail` и т.д.).
3. **Синхронный клиент (`MoyskladClient`)**:
   - Расположение: [moysklad/client/sync_client.py](moysklad/client/sync_client.py)
   - Функционал: Использует `httpx.Client` для выполнения блокирующих сетевых запросов. Инициализирует синхронные группы API.
4. **Базовые конечные точки (`AsyncEndpoint` и `SyncEndpoint`)**:
   - Расположение: [moysklad/api/base.py](moysklad/api/base.py)
   - Функционал: Обобщенные (Generic) классы, которые оборачивают вызовы к конкретным API. Реализуют стандартные методы:
     - `get(uuid, expand)` — получение сущности по её UUID.
     - `list(limit, offset, expand, filter)` — получение списка сущностей с пагинацией и фильтрацией. Возвращает модель `ListResponse[T]`.
     - `iter_all(expand, filter, chunk_size)` — генератор (асинхронный или синхронный) для ленивой итерации по всем записям с автоматической пагинацией.
     - `create(data)` — создание сущности. Принимает словарь или Pydantic-модель, отправляет POST-запрос, возвращает провалидированную модель.
     - `metadata()` — получение метаданных для данной группы сущностей (`GET /path/metadata`).
     - `export(uuid, template)` — печать/экспорт документа (`POST /path/{uuid}/export`).
     - `images(uuid)` — получение изображений (`GET /path/{uuid}/images`).
5. **Группы API**:
   - Каждая группа API (например, `entity`, `document`, `report`) содержит класс, инициализирующий конечные точки.
   - Пример: в [moysklad/api/entity/__init__.py](moysklad/api/entity/__init__.py) определены классы `AsyncEntityAPI` и `SyncEntityAPI`. Они содержат свойства (например, `self.product`), которые являются экземплярами `AsyncEndpoint[Product]` и `SyncEndpoint[Product]` соответственно.

> [!IMPORTANT]
> Обратите внимание, что API МойСклад размещает **документы** по путям вида `entity/customerorder`, а не `document/customerorder`. Поэтому при создании конечных точек в [moysklad/api/document/__init__.py](moysklad/api/document/__init__.py) базовым путем передается `"entity/customerorder"`, `"entity/invoiceout"` и т.д.

---

## 📦 Модели данных (Pydantic v2)

Все входящие и исходящие данные валидируются с помощью **Pydantic v2**.

1. **Базовые модели**:
   - Расположение: [moysklad/models/base.py](moysklad/models/base.py)
   - Ключевые классы:
     - `Meta` — общие метаданные МойСклад (содержат `href`, `type`, `mediaType` и т.д.).
     - `ListResponse[T]` — универсальная обёртка для ответов API со списком объектов (содержит `context`, `meta` и `rows: list[T]`).
     - `BaseEntity` — базовый класс для справочников/сущностей (наследуется от Pydantic `BaseModel`). Включает обязательные поля: `meta`, `id`, `accountId`, `updated`, `name`.
     - `BaseDocument` — базовый класс для документов (наследуется от `BaseEntity`). Включает поля: `moment`, `applicable`, `sum`, `description`, `state`, `organization`.
2. **Структура моделей на диске**:
   - `moysklad/models/entity/` — модели справочников (товары, контрагенты и др.).
   - `moysklad/models/document/` — модели документов (заказы, счета, отгрузки и др.).
   - `moysklad/models/retail/`, `moysklad/models/report/`, `moysklad/models/webhook/` и т.д.

---

## 🛠 Пошаговый гайд: Как добавить новую сущность или документ

Когда вам нужно добавить поддержку новой сущности из API МойСклад 1.2 (например, `entity/new_item`):

### Шаг 1: Создание модели данных
Создайте файл в соответствующей директории моделей, например `moysklad/models/entity/new_item.py`:
```python
from moysklad.models.base import BaseEntity

class NewItem(BaseEntity):
    # Добавьте специфичные для этой сущности поля Pydantic
    description: str | None = None
    code: str | None = None
    externalCode: str
```

### Шаг 2: Регистрация конечной точки в API-группе
Откройте соответствующий API-файл инициализации, например [moysklad/api/entity/__init__.py](moysklad/api/entity/__init__.py), и добавьте:
1. Импорт модели:
   ```python
   from moysklad.models.entity.new_item import NewItem
   ```
2. Инициализацию в `AsyncEntityAPI`:
   ```python
   self.new_item = AsyncEndpoint[NewItem](client, "entity/new_item", NewItem)
   ```
3. Инициализацию в `SyncEntityAPI`:
   ```python
   self.new_item = SyncEndpoint[NewItem](client, "entity/new_item", NewItem)
   ```

После этого конечная точка станет доступна через:
```python
# Асинхронно
item = await client.entity.new_item.get("uuid")
# Синхронно
item = client.entity.new_item.get("uuid")
```

---

## 🔍 Фильтрация и запросы

Для фильтрации используется класс-строитель `Filter`, экспортируемый из корня пакета.
- Расположение: [moysklad/utils/filters.py](moysklad/utils/filters.py)
- Доступные методы фильтрации:
  - `eq(field, value)` — равно (`=`)
  - `neq(field, value)` — не равно (`!=`)
  - `gt(field, value)` — больше (`>`)
  - `lt(field, value)` — меньше (`<`)
  - `gte(field, value)` — больше или равно (`>=`)
  - `lte(field, value)` — меньше или равно (`<=`)
  - `contains(field, value)` — частичное совпадение (`~`)

Пример использования:
```python
from moysklad import AsyncMoyskladClient
from moysklad.utils.filters import Filter

client = AsyncMoyskladClient(token="...")
f = Filter().eq("archived", False).contains("name", "Смартфон")

# Передаём объект Filter в метод list или iter_all
products = await client.entity.product.list(filter=f)
```

---

## ⚠️ Обработка ошибок

При выполнении запросов могут возникать следующие исключения (все они наследуются от `MoyskladError` из [moysklad/client/exceptions.py](moysklad/client/exceptions.py)):

- `AuthError` — ошибка авторизации (HTTP 401). Неверный токен или логин/пароль.
- `RateLimitError` — превышение лимита запросов (HTTP 429).
- `APIError` — общая ошибка API МойСклад (HTTP 400, 404, 500 и т.д.). Содержит `status_code` и `details` (с деталями ошибки от МоегоСклада).

Пример обработки ошибок:
```python
from moysklad import AsyncMoyskladClient
from moysklad.client.exceptions import APIError, RateLimitError

try:
    product = await client.entity.product.get("non-existent-uuid")
except APIError as e:
    print(f"Ошибка API (код {e.status_code}): {e.details}")
except RateLimitError:
    print("Превышен лимит запросов!")
```

---

## 🧪 Разработка, тестирование и линтинг

### Установка окружения для разработки
1. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для macOS/Linux
   ```
2. Установите библиотеку с зависимостями для разработки:
   ```bash
   pip install -e .[dev]
   ```

### Запуск тестов
Проект использует `pytest` и `respx` для юнит-тестирования без реальных запросов в сеть.
- Запустить все тесты:
   ```bash
   pytest
   ```
- Запустить интеграционный тест (требует реальный токен в переменной окружения `MOYSKLAD_TOKEN`):
   ```bash
   MOYSKLAD_TOKEN="your_actual_token" python integration_test.py
   ```

### Линтинг и форматирование кода
Используются инструменты `ruff` и `mypy` для проверки стилистики и типов:
- Запуск линтера:
   ```bash
   ruff check .
   ```
- Форматирование кода:
   ```bash
   ruff format .
   ```
- Статический анализ типов:
   ```bash
   mypy moysklad
   ```
