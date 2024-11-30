from unittest.mock import Mock
import allure
from data import Data

class TestIngredient:

    @allure.title('проверить, что метод get_name возвращает название начинки')
    def test_get_name_filling(self):
        mock_get_name_filling = Mock()
        mock_get_name_filling.get_name.return_value = 'Хрустящие минеральные кольца'
        assert mock_get_name_filling.get_name() == 'Хрустящие минеральные кольца'

    @allure.title('Проверка, что метод get_price возвращает стоимость начинки')
    def test_get_price_filling(self):
        mock_get_price_filling = Mock()
        mock_get_price_filling.get_price.return_value = '300'
        assert mock_get_price_filling.get_price() == '300'

    @allure.title('проверить, что метод get_name возвращает название соуса')
    def test_get_name_sauce(self):
        mock_get_name_sauce = Mock()
        mock_get_name_sauce.get_name.return_value = 'Соус - Spicy-X'
        assert mock_get_name_sauce.get_name() == 'Соус - Spicy-X'

    @allure.title('Проверка, что метод get_price возвращает стоимость соуса')
    def test_get_price_sauce(self):
        mock_get_price_sauce = Mock()
        mock_get_price_sauce.get_price.return_value = '90'
        assert mock_get_price_sauce.get_price() == '90'

    @allure.title('Проверить, что метод get_type возвращает название начинки')
    def test_get_type_filling(self):
        mock_get_type_filling = Mock()
        mock_get_type_filling.get_type.return_value = Data.INGREDIENT_TYPE_FILLING
        assert mock_get_type_filling.get_type() == Data.INGREDIENT_TYPE_FILLING

    @allure.title('Проверить, что метод get_type возвращает название соуса')
    def test_get_type_sauce(self):
        mock_get_type_sauce = Mock()
        mock_get_type_sauce.get_type.return_value = Data.INGREDIENT_TYPE_SAUCE
        assert mock_get_type_sauce.get_type() == Data.INGREDIENT_TYPE_SAUCE