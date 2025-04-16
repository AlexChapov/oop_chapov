from unittest.mock import patch

import pytest

from src.categories_and_products import Category, Product


@pytest.fixture()
def products_samsung() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def product_iphone() -> Product:
    return Product("Iphone", "Nano-Sim + eSim, 512Gb, Black", 104000, 2)


def test_init_products(products_samsung: Product) -> None:
    assert products_samsung.name == "Samsung Galaxy S23 Ultra"
    assert products_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert products_samsung.price == 180000
    assert products_samsung.quantity == 5


def test_set_negative_price(products_samsung: Product) -> None:
    products_samsung.price = -100.0
    assert products_samsung.price == 180000.0


def test_set_zero_price(products_samsung: Product) -> None:
    products_samsung.price = 0
    assert products_samsung.price == 180000.0


def test_category_store_products_count(products_samsung, product_iphone):
    category = Category("SmartPhones", "", [product_iphone, products_samsung])
    products_count = products_samsung.quantity + product_iphone.quantity
    assert category.product_count == products_count


def test_new_product_creation() -> None:
    product_data = {"name": "Test Product", "description": "Description", "price": 100.0, "quantity": 5}
    product = Product.new_product(product_data)
    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.quantity == 5


def test_set_lower_price_without_confirm(products_samsung: Product) -> None:
    with patch("builtins.input", return_value="n"):
        products_samsung.price = 150000
        assert products_samsung.price == 150000
