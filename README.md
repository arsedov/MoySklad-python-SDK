# moysklad-python

Асинхронная и синхронная библиотека для работы с API МойСклад 1.2.

## Установка через Git

Для использования в ваших проектах:
```bash
pip install git+https://github.com/ВАШ_АККАУНТ/ВАШ_РЕПОЗИТОРИЙ.git
```
(Замените URL на ваш репозиторий).

## Пример использования (FastAPI)

```python
from fastapi import FastAPI
from moysklad import AsyncMoyskladClient

app = FastAPI()
client = AsyncMoyskladClient(token="your_moysklad_token")

@app.get("/products")
async def get_products():
    # Запрашиваем 10 товаров
    products = await client.entity.product.list(limit=10)
    return products
```
