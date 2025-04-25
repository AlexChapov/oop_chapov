class Product:
    """Класс 'Продукты' со свойствами и методами"""

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
        """Создает продукт из словаря с данными."""
        return cls(**product_data)

    @property
    def price(self) -> float:
        """Геттер для приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для приватного атрибута цены."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __add__(self, other):
        """Реализует сложение стоимости двух продуктов, если типы совпадают."""
        if not isinstance(other, self.__class__):
            raise TypeError("Нельзя складывать продукты разных типов")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self) -> str:
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    """Класс для представления смартфонов, наследуется от Product."""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        """Строковое представление для смартфона."""
        return super().__str__() + f", Модель: {self.model}, Эффективность: {self.efficiency}%"


class LawnGrass(Product):
    """Класс для представления газонной травы, наследуется от Product."""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        """Строковое представление для газонной травы."""
        return super().__str__() + f", Страна: {self.country}, Период прорастания: {self.germination_period}, Цвет: {self.color}"


class Category:
    """Класс 'Категории продуктов'"""

    name: str  # название
    description: str  # описание
    __products: list[Product]  # список товаров категории

    _category_count = 0  # Счетчик категорий
    _product_count = 0  # Счетчик количества товаров

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category._category_count += 1
        Category._product_count += sum(p.quantity for p in products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию, проверяя тип."""
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError("Можно добавлять только объекты типа Product, Smartphone, LawnGrass или их наследников")
        self.__products.append(product)
        Category._product_count += product.quantity

    @property
    def products(self) -> list:
        """Возвращает список продуктов в виде строки."""
        return [str(product) for product in self.__products]

    @property
    def product_count(self):
        """Считает общее количество товаров."""
        return sum(product.quantity for product in self.__products)

    @staticmethod
    def get_category_count():
        """Считает общее количество категорий."""
        return Category._category_count

    @staticmethod
    def get_product_count():
        """Возвращает общее количество всех товаров всех категорий."""
        return Category._product_count

    def __str__(self) -> str:
        """Выводит название категории и общее количество товаров в ней."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
