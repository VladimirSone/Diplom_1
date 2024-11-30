from unittest.mock import Mock
import pytest
from conftest import mock_bun, mock_sauce, mock_filling
from data import Data
from yandex_practicum.burger import Burger
import allure


class TestBurger:

    @allure.title('Проверить, что метод set_buns добавляет булочку в бургер')
    def test_set_burgers(self):
        burger = Burger()
        mock_set_burgers = Mock()
        mock_set_burgers.set_buns.return_value = mock_set_burgers
        burger.set_buns = mock_set_burgers
        assert burger.set_buns == mock_set_burgers

    @allure.title('Проверить, что метод add_ingredient добавляет ингредиенты (соусы и начинки) в бургер')
    @pytest.mark.parametrize('ingredients, added_ingredient', [[Data.SAUCE_NAME, Data.SAUCE_NAME], [Data.FILLING_NAME, Data.FILLING_NAME]])
    def test_add_ingredient_success(self, ingredients, added_ingredient):
        burger = Burger()
        burger.add_ingredient(ingredients)
        assert burger.ingredients == [added_ingredient] and len(burger.ingredients) == 1

    @allure.title('Проверить, что метод remove_ingredient удаляет ингредиент (соус и/или начинку) из бургера')
    @pytest.mark.parametrize('ingredients, removed_ingredient', [[Data.SAUCE_NAME, Data.SAUCE_NAME], [Data.FILLING_NAME, Data.FILLING_NAME]])
    def test_remove_ingredient_success(self, ingredients, removed_ingredient, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(1)
        assert removed_ingredient not in burger.ingredients and mock_filling in burger.ingredients

    @allure.title('Проверить, что метод move_ingredient перемещает ингредиенты в бургере')
    def test_move_ingredient_success(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling and burger.ingredients[1] == mock_sauce

    @allure.title('Проверить, что метод get_price считает итоговую сумму бургера')
    def test_get_price_burger_success(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == Data.burger_final_cost

    @allure.title('Проверить, что метод get_receipt получает рецепт бургера и его стоимость')
    def test_get_receipt_success(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert (burger.get_receipt() ==
        ("(==== Краторная булка N-200i ====)\n" "= sauce Соус традиционный галактический =\n"
        "= filling Мясо бессмертных моллюсков Protostomia =\n"
        "(==== Краторная булка N-200i ====)\n" "\n"f"Price: {burger.get_price()}"))
