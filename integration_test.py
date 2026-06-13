import asyncio
import os
from moysklad import AsyncMoyskladClient

async def run_tests():
    # Попробуем прочитать токен из переменной окружения
    token = os.getenv("MOYSKLAD_TOKEN", "ВАШ_ТЕСТОВЫЙ_ТОКЕН")
    
    if token == "ВАШ_ТЕСТОВЫЙ_ТОКЕН":
        print("Пожалуйста, установите токен в переменной окружения MOYSKLAD_TOKEN или замените его в коде.")
        return

    client = AsyncMoyskladClient(token=token)
    
    print("=== Запуск интеграционных тестов ===")
    
    # 1. Проверка Entity API (Товары)
    try:
        print("\n[1] Тестирование Entity API (Товары)...")
        products = await client.entity.product.list(limit=1)
        print(f"Успешно. Найдено товаров: {len(products.rows)}")
        if products.rows:
            print(f"Пример товара: {products.rows[0].name}")
    except Exception as e:
        print(f"Ошибка при получении товаров: {e}")

    # 2. Проверка Document API (Заказы покупателя)
    try:
        print("\n[2] Тестирование Document API (Заказы покупателя)...")
        orders = await client.document.customerorder.list(limit=1)
        print(f"Успешно. Найдено заказов: {len(orders.rows)}")
    except Exception as e:
        print(f"Ошибка при получении заказов: {e}")

    # 3. Проверка Report API (Остатки)
    try:
        print("\n[3] Тестирование Report API (Остатки)...")
        stock = await client.report.stock.all.list(limit=1)
        print(f"Успешно. Получен отчет по остаткам. Записей: {len(stock.rows)}")
    except Exception as e:
        print(f"Ошибка при получении отчета по остаткам: {e}")

    # 4. Проверка Metadata API
    try:
        print("\n[4] Тестирование Metadata API (Метаданные заказа покупателя)...")
        meta = await client.document.customerorder.metadata()
        states = meta.get("states", [])
        print(f"Успешно. Найдено статусов заказов: {len(states)}")
    except Exception as e:
        print(f"Ошибка при получении метаданных: {e}")

    print("\n=== Тестирование завершено ===")

if __name__ == "__main__":
    asyncio.run(run_tests())
