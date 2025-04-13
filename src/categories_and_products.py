class Product:
    """Класс 'Продукты' со свойствами указанными ниже"""

    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name: str, description: str, price: float = 0, quantity: int = 0) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс 'Категории продуктов' со свойствами указанными ниже"""

    name: str  # название
    description: str  # описание
    products: list[Product]  # список товаров категории

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products) -> None:

        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
