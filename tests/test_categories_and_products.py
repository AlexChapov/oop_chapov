import pytest
from src.categories_and_products import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def product1():
    """Создает тестовый продукт для использования в тестах."""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    """Создает тестовый продукт для использования в тестах."""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product3():
    """Создает тестовый продукт для использования в тестах."""
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def smartphone1():
    """Создает тестовый смартфон для использования в тестах."""
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    """Создает тестовый смартфон для использования в тестах."""
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def grass1():
    """Создает тестовый продукт типа газонная трава для использования в тестах."""
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2():
    """Создает тестовый продукт типа газонная трава для использования в тестах."""
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category(smartphone1, smartphone2, grass1, grass2):
    """Создает тестовую категорию товаров для использования в тестах."""
    return Category(
        "Смартфоны и газонная трава",
        "Высокотехнологичные смартфоны и элитная газонная трава",
        [smartphone1, smartphone2, grass1, grass2],
    )


def test_product_str(product1):
    """Тестирует строковое представление продукта."""
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_smartphone_str(smartphone1):
    """Тестирует строковое представление смартфона."""
    assert (
        str(smartphone1)
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт., Модель: S23 Ultra, Эффективность: 95.5%"
    )


def test_grass_str(grass1):
    """Тестирует строковое представление газонной травы."""
    assert (
        str(grass1)
        == "Газонная трава, 500.0 руб. Остаток: 20 шт., Страна: Россия, Период прорастания: 7 дней, Цвет: Зеленый"
    )


def test_product_addition(product1, product2, product3):
    """Тестирует операцию сложения товаров."""
    assert product1 + product2 == 180000.0 * 5 + 210000.0 * 8
    assert product1 + product3 == 180000.0 * 5 + 31000.0 * 14
    assert product2 + product3 == 210000.0 * 8 + 31000.0 * 14


def test_product_price_setter_valid(product1):
    """Тестирует корректную установку цены товара."""
    product1.price = 190000
    assert product1.price == 190000


def test_product_price_setter_invalid(product1, capsys):
    """Тестирует установку некорректной цены товара (отрицательной или нулевой)."""
    product1.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product1.price == 180000.0

    product1.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product1.price == 180000.0


def test_category_product_list(category):
    """Тестирует список продуктов в категории."""
    products_str = category.products
    assert isinstance(products_str, list)
    assert all(isinstance(p, str) for p in products_str)
    assert "Samsung Galaxy S23 Ultra" in products_str[0]


def test_add_product_to_category(category):
    """Тестирует добавление нового продукта в категорию."""
    initial_count = category.product_count
    new_product = Product("Test", "Some desc", 1000.0, 3)
    category.add_product(new_product)
    assert category.product_count == initial_count + 3


def test_add_invalid_product_to_category(category):
    """Тестирует добавление неправильного типа объекта в категорию."""
    try:
        category.add_product("Not a product")
    except TypeError:
        pass
    else:
        assert False, "TypeError не был поднят при добавлении неправильного типа объекта"


def test_create_logger_mixin(capsys):
    """Тестирует работу миксина логирования при создании объекта."""
    Product("Test Product", "Описание продукта", 1200.0, 10)

    captured = capsys.readouterr()

    assert "Создан объект класса Product с аргументами: ('Test Product', 'Описание продукта', 10)" in captured.out
    assert "и именованными аргументами: {}" in captured.out
    assert "Test Product" in captured.out
    assert "Описание продукта" in captured.out
    assert "10" in captured.out


def test_repr(product1):
    """Тестирует корректность представления объекта в виде строки."""
    assert repr(product1) == "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)"
    product_zero_price = Product("Test Product", "Описание продукта", 0, 10)
    assert repr(product_zero_price) == "Product('Test Product', 'Описание продукта', без цены, 10)"


def test_create_product_with_zero_quantity():
    """Тестирует создание продукта с нулевым количеством (выбрасывание ValueError)."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_category_middle_price_empty_category(category):
    """Тестирует вычисление средней цены для категории без товаров."""
    empty_category = Category("Пустая категория", "Категория без продуктов", [])
    assert empty_category.middle_price() == 0


def test_category_middle_price(category):
    """Тестирует вычисление средней цены для категории с товарами."""
    assert category.middle_price() > 0
