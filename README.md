# МойСклад Python SDK

**100% покрывающий (Full-Fledged) SDK** для работы с API МойСклад 1.2 (JSON API).
Поддерживает как асинхронные (`httpx.AsyncClient`, идеально для FastAPI), так и синхронные (`httpx.Client`, идеально для Django/Celery) вызовы.

> [!NOTE]
> **Для ИИ-агентов и разработчиков:** В корне репозитория доступен специальный гайд [AI.md](AI.md) с описанием архитектуры, структуры моделей и инструкцией по расширению SDK.

В библиотеке реализованы все 90+ сущностей из документации (Документы, Справочники, Розничные операции, Отчеты, Метаданные, Вебхуки, Корзина, Аудит и Экспорт/Печать).

## Установка через Git

Для использования в ваших проектах:
```bash
pip install git+https://github.com/arsedov/MoySklad-python-SDK.git
```

## Пример использования (Асинхронный - FastAPI)

```python
import asyncio
from moysklad import AsyncMoyskladClient

async def main():
    # Клиент поддерживает асинхронный контекст-менеджер (соединения закроются сами).
    async with AsyncMoyskladClient(token="your_moysklad_token") as client:

        # 1. Получение товаров (Entity API) с пагинацией
        products = await client.entity.product.list(limit=10, offset=0)
        print(f"Загружено товаров: {len(products.rows)}")

        # 2. Создание / обновление / удаление товара
        created = await client.entity.product.create({"name": "Новый товар"})
        updated = await client.entity.product.update(created.id, {"name": "Переименован"})
        await client.entity.product.delete(updated.id)

        # 3. Массовые операции (один запрос на пачку)
        await client.entity.product.create_bulk([{"name": "A"}, {"name": "B"}])
        await client.entity.product.delete_bulk([created.id, updated.id])

        # 4. Полная выгрузка через генератор (учитывает meta.size)
        async for product in client.entity.product.iter_all():
            ...

        # 5. Отчеты по остаткам (Report API)
        stock = await client.report.stock.all.list()

        # 6. Экспорт документа в PDF (Print API)
        # await client.document.invoiceout.export("uuid", template={"id": "..."})

if __name__ == "__main__":
    asyncio.run(main())
```

## Пример использования (Синхронный - Django / Скрипты)

```python
from moysklad import MoyskladClient, Filter

# Таймаут и число повторов при 429 настраиваются:
client = MoyskladClient(token="your_moysklad_token", timeout=30.0, max_retries=3)

# Получение информации о компании (Context API)
settings = client.context.companysettings()

# Загрузка заказов покупателей с фильтрами (билдер — fluent, через цепочку):
f = Filter().eq("name", "12345").gt("sum", 1000)
orders = client.document.customerorder.list(filter=f)

client.close()  # либо: with MoyskladClient(token=...) as client: ...
```

> При ответе `429 Too Many Requests` клиент автоматически повторяет запрос,
> учитывая заголовок `X-RateLimit-Retry-After` (до `max_retries` раз).

## Структура SDK
- `client.entity` — Все справочники (Товары, Контрагенты, Организации, Договоры, Комплекты, Серии и т.д.).
- `client.document` — Все документы (Заказы, Счета, Отгрузки, Инвентаризации, Перемещения, Возвраты, Кассовые ордера и т.д.).
- `client.retail` — Розница (Точки продаж, Смены, Розничные продажи).
- `client.report` — Отчеты (Остатки, Продажи).
- `client.bonus_program` — Бонусные программы.
- `client.webhook` — Вебхуки.
- `client.context` — Настройки пользователя и компании.
- `client.trash` — Управление корзиной.
- `client.audit` — Аудит (история действий).
- `client.async_task` — Управление асинхронными задачами API.
