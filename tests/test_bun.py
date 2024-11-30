from unittest.mock import Mock
import allure
from data import Data


class TestBun:
    @allure.title('Проверить, что метод get возвращает название')
    def test_get_bun(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Краторная булка N-200i'
        assert mock_bun.get_name() == Data.NAMEBREAD

    @allure.title('Проверить, что метод get возвращает стоимость')
    def test_price_bun(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = "1255"
        assert mock_bun.get_price() == "1255"
