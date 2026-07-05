# E-commerce project

Проект для домашнего задания по ООП.

## Описание

В проекте реализованы базовые сущности интернет-магазина:

- `Product` — товар;
- `Category` — категория товаров.

## Класс `Product`

Класс `Product` описывает товар.

Атрибуты:

- `name` — название товара;
- `description` — описание товара;
- `price` — цена товара;
- `quantity` — количество товара в наличии.

Пример:

```python
from src.classes import Product

product = Product(
    name="Samsung Galaxy S23 Ultra",
    description="256GB, Серый цвет, 200MP камера",
    price=180000.0,
    quantity=5,
)
