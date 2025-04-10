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
    products: list  # список товаров категории

    number_of_categories = []
    number_of_products = []

    def __init__(self, name: str, description: str) -> None:

        self.name = name
        self.description = description
        self.products = []

        Category.number_of_categories += 1
