import pytest

from src.classes import Category, Product


@pytest.fixture(autouse=True)
def reset_category_counters() -> None:
    """Сбрасывает счетчики категорий и товаров перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def product() -> Product:
    """Возвращает тестовый товар."""
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product() -> Product:
    """Возвращает второй тестовый товар."""
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
    )


def test_product_initialization(product: Product) -> None:
    """Тестирует корректную инициализацию товара."""
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_initialization(
    product: Product,
    second_product: Product,
) -> None:
    """Тестирует корректную инициализацию категории."""
    category = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации",
        products=[product, second_product],
    )

    assert category.name == "Смартфоны"
    assert category.description == (
        "Смартфоны, как средство не только коммуникации"
    )
    assert category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_category_count(
    product: Product,
    second_product: Product,
) -> None:
    """Тестирует подсчет количества категорий."""
    Category(
        name="Смартфоны",
        description="Смартфоны, как средство коммуникации",
        products=[product],
    )
    Category(
        name="Телевизоры",
        description="Современные телевизоры",
        products=[second_product],
    )

    assert Category.category_count == 2


def test_product_count(
    product: Product,
    second_product: Product,
) -> None:
    """Тестирует подсчет количества товаров в категориях."""
    Category(
        name="Смартфоны",
        description="Смартфоны, как средство коммуникации",
        products=[product, second_product],
    )
    Category(
        name="Аксессуары",
        description="Аксессуары для смартфонов",
        products=[],
    )

    assert Category.product_count == 2


def test_empty_category_products() -> None:
    """Тестирует категорию без товаров."""
    category = Category(
        name="Аксессуары",
        description="Аксессуары для смартфонов",
        products=[],
    )

    assert category.products == ""
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product(product: Product, second_product: Product) -> None:
    """Тестирует добавление товара в категорию."""
    category = Category(
        name="Смартфоны",
        description="Смартфоны, как средство коммуникации",
        products=[product],
    )

    category.add_product(second_product)

    assert category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )
    assert Category.product_count == 2


def test_new_product() -> None:
    """Тестирует создание товара через класс-метод."""
    product_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14,
    }

    product = Product.new_product(product_data)

    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14


def test_price_setter_positive_value(product: Product) -> None:
    """Тестирует установку положительной цены."""
    product.price = 190000.0

    assert product.price == 190000.0


def test_price_setter_zero_value(
    product: Product,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Тестирует запрет установки нулевой цены."""
    product.price = 0

    captured = capsys.readouterr()

    assert product.price == 180000.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_setter_negative_value(
    product: Product,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Тестирует запрет установки отрицательной цены."""
    product.price = -100

    captured = capsys.readouterr()

    assert product.price == 180000.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_str(product: Product) -> None:
    """Тестирует строковое представление товара."""
    assert str(product) == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    )


def test_category_str(
    product: Product,
    second_product: Product,
) -> None:
    """Тестирует строковое представление категории."""
    category = Category(
        name="Смартфоны",
        description="Смартфоны, как средство коммуникации",
        products=[product, second_product],
    )

    assert str(category) == "Смартфоны, количество продуктов: 13 шт."


def test_product_add(
    product: Product,
    second_product: Product,
) -> None:
    """Тестирует сложение товаров."""
    result = product + second_product

    assert result == 2580000.0
