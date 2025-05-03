from abc import ABC, abstractmethod


class CreateLoggerMixin:
    """Миксин для логирования создания объекта."""

    def __init__(self, *args, **kwargs):
        cls_name = self.__class__.__name__
        print(f"Создан объект класса {cls_name} с аргументами: {args} и именованными аргументами: {kwargs}")


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    name: str
    description: str
    quantity: int

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class Product(CreateLoggerMixin, BaseProduct):
    """Класс 'Продукты' со свойствами и методами."""

    def __init__(self, name: str, description: str, price: float = 0, quantity: int = 0) -> None:
        super().__init__(name, description, quantity)
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = price

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("Нельзя складывать продукты разных типов")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        price_repr = "без цены" if self.price == 0 else self.price
        return f"Product('{self.name}', '{self.description}', {price_repr}, {self.quantity})"


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        return super().__str__() + f", Модель: {self.model}, Эффективность: {self.efficiency}%"


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        return (
            super().__str__()
            + f", Страна: {self.country}, Период прорастания: {self.germination_period}, Цвет: {self.color}"
        )


class Category:
    """Класс 'Категория продуктов'"""

    _category_count = 0
    _product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category._category_count += 1
        Category._product_count += sum(p.quantity for p in products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, (Product, Smartphone, LawnGrass)):
            raise TypeError("Можно добавлять только объекты типа Product, Smartphone, LawnGrass или их наследников")
        self.__products.append(product)
        Category._product_count += product.quantity

    @property
    def products(self) -> list:
        return [str(product) for product in self.__products]

    @property
    def product_count(self):
        return sum(product.quantity for product in self.__products)

    def middle_price(self) -> float:
        try:
            total_price = sum(product.price * product.quantity for product in self.__products)
            total_quantity = sum(product.quantity for product in self.__products)
            return total_price / total_quantity
        except ZeroDivisionError:
            return 0

    @staticmethod
    def get_category_count():
        return Category._category_count

    @staticmethod
    def get_product_count():
        return Category._product_count

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
