class Product:
    """Класс 'Продукты' со свойствами указанными ниже"""

    name: str  # название
    description: str  # описание
    __price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name: str, description: str, price: float = 0, quantity: int = 0) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data):
        """Принимает на вход параметры товара в словаре и возвращает созданный объект класса Product"""
        name = product_data.get("name") or ""
        description = product_data.get("description") or ""
        price = product_data.get("price", 0.0)
        quantity = product_data.get("quantity", 0)

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """
        Геттер для приватного атрибута цены.
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для приватного атрибута цены.
        Реализует проверку:
        в случае если цена равна или ниже нуля, выводит сообщение в консоль
        “Цена не должна быть нулевая или отрицательная”"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            return


class Category:
    """Класс 'Категории продуктов' со свойствами указанными ниже"""

    name: str  # название
    description: str  # описание
    __products: list[Product]  # список товаров категории

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += sum(product.quantity for product in products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list:
        """Возвращает список товаров"""
        formatted_list = []
        for product in self.__products:
            formatted_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return formatted_list
