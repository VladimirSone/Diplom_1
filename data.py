from yandex_practicum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Data:
    NAMEBREAD = 'Краторная булка N-200i'
    PRICE = '1255'
    INGREDIENT_TYPE_SAUCE = 'SAUCE'
    INGREDIENT_TYPE_FILLING = 'FILLING'
    SAUCE_NAME = 'Соус традиционный галактический'
    SAUCE_PRICE = '15'
    FILLING_NAME = 'Мясо бессмертных моллюсков Protostomia'
    FILLING_PRICE = '1350'
    burger_final_cost = PRICE * 2 + SAUCE_PRICE + FILLING_PRICE

class DataBase:
    test_data_base_buns = [
        [0, 'black bun', 100],
        [1, 'white bun', 200],
        [2, 'red bun', 300]]

    test_data_base_ingredients = [
        [0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100],
        [1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200],
        [2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300],
        [3, INGREDIENT_TYPE_FILLING, 'cutlet', 100],
        [4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200],
        [5, INGREDIENT_TYPE_FILLING, 'sausage', 300]]
