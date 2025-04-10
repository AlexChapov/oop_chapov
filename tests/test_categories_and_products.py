import pytest

from src.categories_and_products import Category, Product


@pytest.fixture()
def products_samsung() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_products(products_samsung: Product) -> None:
    assert products_samsung.name == "Samsung Galaxy S23 Ultra"
    assert products_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert products_samsung.price == 180000
    assert products_samsung.quantity == 5


@pytest.fixture()
def category_phone() -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        # ["product1", "product2", "product3"],
    )


def test_init_category(category_phone: Category) -> None:

    assert category_phone.name == "Смартфоны"
    assert (
        category_phone.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert Category.number_of_categories == 1
