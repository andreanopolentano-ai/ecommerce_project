from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов."""

    name: str
    description: str
    quantity: int

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        """Инициализирует базовые атрибуты продукта."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Возвращает цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Устанавливает новую цену товара."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        self.__price = new_price

    @classmethod
    @abstractmethod
    def new_product(cls, product: dict[str, Any]) -> "BaseProduct":
        """Создает новый товар из словаря."""

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление товара."""

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Складывает товары."""


class PrintMixin:
    """Миксин для вывода информации о создании объекта."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализирует объект и выводит информацию о нем."""
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self) -> str:
        """Возвращает техническое представление объекта."""
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.description!r}, "
            f"{self.price!r}, {self.quantity!r})"
        )


class Product(PrintMixin, BaseProduct):
    """Класс для описания товара."""

    @classmethod
    def new_product(cls, product: dict[str, Any]) -> "Product":
        """Создает новый товар из словаря."""
        return cls(
            name=product["name"],
            description=product["description"],
            price=product["price"],
            quantity=product["quantity"],
        )

    def __str__(self) -> str:
        """Возвращает строковое представление товара."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: BaseProduct) -> float:
        """Возвращает общую стоимость товаров одного класса."""
        if type(self) is not type(other):
            raise TypeError("Складывать можно только товары одного класса")

        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """Класс для описания смартфона."""

    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализирует объект смартфона."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для описания газонной травы."""

    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализирует объект газонной травы."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс для описания категории товаров."""

    name: str
    description: str

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        """Инициализирует объект категории товаров."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар или наследника товара в категорию."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает список товаров категории в виде строки."""
        products_str = ""

        for product in self.__products:
            products_str += f"{str(product)}\n"

        return products_str

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        total_quantity = 0

        for product in self.__products:
            total_quantity += product.quantity

        return f"{self.name}, количество продуктов: {total_quantity} шт."
