import pytest
from src.categories_and_products import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category(smartphone1, smartphone2, grass1, grass2):
    return Category(
        "Смартфоны и газонная трава",
        "Высокотехнологичные смартфоны и элитная газонная трава",
        [smartphone1, smartphone2, grass1, grass2],
    )


def test_product_str(product1):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_smartphone_str(smartphone1):
    assert (
        str(smartphone1)
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт., Модель: S23 Ultra, Эффективность: 95.5%"
    )


def test_grass_str(grass1):
    assert (
        str(grass1)
        == "Газонная трава, 500.0 руб. Остаток: 20 шт., Страна: Россия, Период прорастания: 7 дней, Цвет: Зеленый"
    )


def test_product_addition(product1, product2, product3):
    assert product1 + product2 == 180000.0 * 5 + 210000.0 * 8
    assert product1 + product3 == 180000.0 * 5 + 31000.0 * 14
    assert product2 + product3 == 210000.0 * 8 + 31000.0 * 14


def test_product_price_setter_valid(product1):
    product1.price = 190000
    assert product1.price == 190000


def test_product_price_setter_invalid(product1, capsys):
    product1.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product1.price == 180000.0

    product1.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product1.price == 180000.0


def test_category_product_list(category):
    products_str = category.products
    assert isinstance(products_str, list)
    assert all(isinstance(p, str) for p in products_str)
    assert "Samsung Galaxy S23 Ultra" in products_str[0]


def test_add_product_to_category(category):
    initial_count = category.product_count
    new_product = Product("Test", "Some desc", 1000.0, 3)
    category.add_product(new_product)
    assert category.product_count == initial_count + 3


def test_add_invalid_product_to_category(category):
    try:
        category.add_product("Not a product")
    except TypeError:
        pass
    else:
        assert False, "TypeError не был поднят при добавлении неправильного типа объекта"
