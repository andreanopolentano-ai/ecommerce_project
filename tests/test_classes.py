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
