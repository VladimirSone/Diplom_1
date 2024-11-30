from unittest.mock import Mock
from data import Data
import pytest


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = Data.NAMEBREAD
    mock_bun.get_price.return_value = Data.PRICE
    return mock_bun

@pytest.fixture
def mock_filling():
    mock_for_filling = Mock()
    mock_for_filling.get_name.return_value = Data.FILLING_NAME
    mock_for_filling.get_price.return_value = Data.FILLING_PRICE
    mock_for_filling.get_type.return_value = Data.INGREDIENT_TYPE_FILLING
    return mock_for_filling

@pytest.fixture
def mock_sauce():
    mock_for_sauce = Mock()
    mock_for_sauce.get_name.return_value = Data.SAUCE_NAME
    mock_for_sauce.get_price.return_value = Data.SAUCE_PRICE
    mock_for_sauce.get_type.return_value = Data.INGREDIENT_TYPE_SAUCE
    return mock_for_sauce
