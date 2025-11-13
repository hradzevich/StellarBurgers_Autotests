import random as r
from data import Ingredients


# Возвращает случайное название ингредиента из списка INGREDIENTS
def random_ingredient():
    return r.choice(Ingredients.INGREDIENTS)

# Проверяет, есть ли точное совпадение order_number в списке orders.
# Если в li есть лишние символы, он ищет среди всех подстрок
def is_order_number_present(orders, order_number):
    order_number_str = str(order_number)
    for item in orders:
        for line in item.split("\n"):
            if line.strip() == order_number_str:
                return True
    return False
