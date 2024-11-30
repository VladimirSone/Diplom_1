from data import DataBase
import pytest
import allure
from yandex_practicum.database import Database


class TestDataBase:
    @allure.title('Проверить, метод available_buns получает список доступных булок из базы')
    @allure.title('Проверить, что получаем имя и стоимость булки')
    @pytest.mark.parametrize('index_bun, bun_name, bun_price', DataBase.test_data_base_buns)
    def test_available_buns_db_success(self, index_bun, bun_name, bun_price):
        database: Database = Database()
        data_buns = database.available_buns()
        assert data_buns[index_bun].get_name() == bun_name and data_buns[index_bun].get_price() == bun_price

    @allure.title('Проверить, что метод available_ingredients получает список доступных ингредиентов из базы')
    @allure.title('Проверить, что получаем имя, тип, стоимость ингредиента')
    @pytest.mark.parametrize('index_i, type_ingredient, name_ingredient, price_ingredient',DataBase.test_data_base_ingredients)
    def test_available_ingredients_db_success(self, index_i, type_ingredient, name_ingredient, price_ingredient):
        database: Database = Database()
        data_ingredients = database.available_ingredients()
        assert (data_ingredients[index_i].get_name() == name_ingredient
                and data_ingredients[index_i].get_type() == type_ingredient
                and data_ingredients[index_i].get_price() == price_ingredient)