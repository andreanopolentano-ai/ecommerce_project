import pytest

from src.classes import BaseProduct, Category, LawnGrass, Product, Smartphone


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


@pytest.fixture
def smartphone() -> Smartphone:
    """Возвращает тестовый смартфон."""
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )


@pytest.fixture
def second_smartphone() -> Smartphone:
    """Возвращает второй тестовый смартфон."""
    return Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )


@pytest.fixture
def lawn_grass() -> LawnGrass:
    """Возвращает тестовую газонную траву."""
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )


@pytest.fixture
def second_lawn_grass() -> LawnGrass:
    """Возвращает вторую тестовую газонную траву."""
    return LawnGrass(
        name="Газонная трава 2",
        description="Выносливая трава для газона",
        price=700.0,
        quantity=15,
        country="США",
        germination_period="5 дней",
        color="Темно-зеленый",
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


def test_smartphone_initialization(smartphone: Smartphone) -> None:
    """Тестирует корректную инициализацию смартфона."""
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawn_grass_initialization(lawn_grass: LawnGrass) -> None:
    """Тестирует корректную инициализацию газонной травы."""
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


def test_add_smartphone_to_category(smartphone: Smartphone) -> None:
    """Тестирует добавление смартфона в категорию."""
    category = Category(
        name="Смартфоны",
        description="Смартфоны и гаджеты",
        products=[],
    )

    category.add_product(smartphone)

    assert category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    )
    assert Category.product_count == 1


def test_add_lawn_grass_to_category(lawn_grass: LawnGrass) -> None:
    """Тестирует добавление газонной травы в категорию."""
    category = Category(
        name="Газонная трава",
        description="Товары для газона",
        products=[],
    )

    category.add_product(lawn_grass)

    assert category.products == (
        "Газонная трава, 500.0 руб. Остаток: 20 шт.\n"
    )
    assert Category.product_count == 1


def test_add_wrong_object_to_category() -> None:
    """Тестирует запрет добавления не продукта в категорию."""
    category = Category(
        name="Смартфоны",
        description="Смартфоны и гаджеты",
        products=[],
    )

    with pytest.raises(TypeError):
        category.add_product("не продукт")  # type: ignore[arg-type]


def test_add_smartphones(
    smartphone: Smartphone,
    second_smartphone: Smartphone,
) -> None:
    """Тестирует сложение смартфонов."""
    result = smartphone + second_smartphone

    assert result == 2580000.0


def test_add_lawn_grass(
    lawn_grass: LawnGrass,
    second_lawn_grass: LawnGrass,
) -> None:
    """Тестирует сложение газонной травы."""
    result = lawn_grass + second_lawn_grass

    assert result == 20500.0


def test_add_different_product_classes(
    smartphone: Smartphone,
    lawn_grass: LawnGrass,
) -> None:
    """Тестирует запрет сложения товаров разных классов."""
    with pytest.raises(TypeError):
        smartphone + lawn_grass


def test_base_product_is_abstract() -> None:
    """Тестирует, что BaseProduct нельзя создать напрямую."""
    with pytest.raises(TypeError):
        BaseProduct(  # type: ignore[abstract]
            name="Базовый продукт",
            description="Описание",
            price=100.0,
            quantity=1,
        )


def test_product_print_mixin(capsys: pytest.CaptureFixture[str]) -> None:
    """Тестирует вывод миксина при создании объекта Product."""
    Product(
        name="Продукт1",
        description="Описание продукта",
        price=1200,
        quantity=10,
    )

    captured = capsys.readouterr()

    assert "Product('Продукт1', 'Описание продукта', 1200, 10)" in captured.out


def test_smartphone_print_mixin(capsys: pytest.CaptureFixture[str]) -> None:
    """Тестирует вывод миксина при создании объекта Smartphone."""
    Smartphone(
        name="Смартфон",
        description="Описание смартфона",
        price=50000,
        quantity=3,
        efficiency=95.5,
        model="S23",
        memory=256,
        color="Черный",
    )

    captured = capsys.readouterr()

    assert "Smartphone('Смартфон', 'Описание смартфона', 50000, 3)" in captured.out


def test_lawn_grass_print_mixin(capsys: pytest.CaptureFixture[str]) -> None:
    """Тестирует вывод миксина при создании объекта LawnGrass."""
    LawnGrass(
        name="Трава",
        description="Описание травы",
        price=500,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый",
    )

    captured = capsys.readouterr()

    assert "LawnGrass('Трава', 'Описание травы', 500, 20)" in captured.out


def test_product_zero_quantity() -> None:
    """Тестирует запрет создания товара с нулевым количеством."""
    with pytest.raises(
        ValueError,
        match="Товар с нулевым количеством не может быть добавлен",
    ):
        Product(
            name="Бракованный товар",
            description="Нельзя добавить",
            price=1000.0,
            quantity=0,
        )


def test_smartphone_zero_quantity() -> None:
    """Тестирует запрет создания смартфона с нулевым количеством."""
    with pytest.raises(
        ValueError,
        match="Товар с нулевым количеством не может быть добавлен",
    ):
        Smartphone(
            name="Смартфон",
            description="Нельзя добавить",
            price=50000.0,
            quantity=0,
            efficiency=95.5,
            model="S23",
            memory=256,
            color="Черный",
        )


def test_category_average_price(
    product: Product,
    second_product: Product,
) -> None:
    """Тестирует расчет среднего ценника товаров категории."""
    category = Category(
        name="Смартфоны",
        description="Смартфоны и гаджеты",
        products=[product, second_product],
    )

    assert category.average_price() == 195000.0


def test_category_middle_price_alias(
    product: Product,
    second_product: Product,
) -> None:
    """Тестирует расчет среднего ценника через middle_price."""
    category = Category(
        name="Смартфоны",
        description="Смартфоны и гаджеты",
        products=[product, second_product],
    )

    assert category.middle_price() == 195000.0


def test_category_average_price_empty_category() -> None:
    """Тестирует расчет среднего ценника для пустой категории."""
    category = Category(
        name="Пустая категория",
        description="Категория без товаров",
        products=[],
    )

    assert category.average_price() == 0


def test_category_middle_price_empty_category() -> None:
    """Тестирует middle_price для пустой категории."""
    category = Category(
        name="Пустая категория",
        description="Категория без товаров",
        products=[],
    )

    assert category.middle_price() == 0
