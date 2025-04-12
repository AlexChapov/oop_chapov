import json
import os

from src.categories_and_products import Category


def load_products_json(operations: str) -> list[Category]:
    full_path = os.path.abspath(operations)
    categories = []
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        for category_data in data:
            try:
                category = Category(category_data["name"], category_data["description"])
                categories.append(category)
            except (KeyError, TypeError, ValueError) as e:
                print(f"Ошибка при обработке данных категории: {category_data}, Ошибка: {e}")
        return categories

    except FileNotFoundError:
        print(f"Ошибка: Файл {full_path} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: Не удалось декодировать JSON-файл {full_path}.")
        return []


print(*load_products_json("../data/products.json"))
