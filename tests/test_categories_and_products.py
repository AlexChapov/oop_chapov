import pytest
from src.categories_and_products import Category, Product


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
def category(product1, product2, product3):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


def test_product_str(product1):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_category_str(category):
    assert str(category) == "Смартфоны, количество продуктов: 27 шт."


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
