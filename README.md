# moysklad-python

Официально **100% покрывающий (Full-Fledged) SDK** для работы с API МойСклад 1.2 (JSON API).
Поддерживает как асинхронные (`httpx.AsyncClient`, идеально для FastAPI), так и синхронные (`httpx.Client`, идеально для Django/Celery) вызовы.

В библиотеке реализованы все 90+ сущностей из документации (Документы, Справочники, Розничные операции, Отчеты, Метаданные, Вебхуки, Корзина, Аудит и Экспорт/Печать).

## Установка через Git

Для использования в ваших проектах:
```bash
pip install git+https://github.com/ВАШ_АККАУНТ/ВАШ_РЕПОЗИТОРИЙ.git
```

## Пример использования (Асинхронный - FastAPI)

```python
import asyncio
from moysklad import AsyncMoyskladClient

async def main():
    client = AsyncMoyskladClient(token="your_moysklad_token")

    # 1. Получение товаров (Entity API) с пагинацией
    products = await client.entity.product.list(limit=10, offset=0)
    print(f"Загружено товаров: {len(products.rows)}")

    # 2. Получение доп. полей заказов (Metadata API)
    meta = await client.document.customerorder.metadata()
    print("Доп. поля заказов:", meta.get("attributes"))

    # 3. Работа с розницей (Retail API)
    shifts = await client.retail.retailshift.list()

    # 4. Отчеты по остаткам (Report API)
    stock = await client.report.stock.all.list()
    
    # 5. Экспорт документа в PDF (Print API)
    # await client.document.invoiceout.export("uuid", template={"id": "..."})

if __name__ == "__main__":
    asyncio.run(main())
```

## Пример использования (Синхронный - Django / Скрипты)

```python
from moysklad import MoyskladClient

client = MoyskladClient(token="your_moysklad_token")

# Получение информации о компании (Context API)
settings = client.context.companysettings()
print(settings.currency)

# Загрузка заказов покупателей с фильтрами
from moysklad.utils.filters import Filter, F
f = Filter()
f.add(F.eq("name", "12345"))
orders = client.document.customerorder.list(filter=f)
```

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
