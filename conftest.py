from unittest.mock import Mock
import pytest
from praktikum.database import Database
from data import Burger1, Burger2


@pytest.fixture
def db():
    return Database()


@pytest.fixture
def mock_bun1():
    mock_of_bun1 = Mock()
    mock_of_bun1.get_name.return_value = Burger1.bun_name
    mock_of_bun1.get_price.return_value = Burger1.bun_price
    return mock_of_bun1


@pytest.fixture
def mock_bun2():
    mock_of_bun2 = Mock()
    mock_of_bun2.get_name.return_value = Burger2.bun_name
    mock_of_bun2.get_price.return_value = Burger2.bun_price
    return mock_of_bun2


@pytest.fixture
def mock_sauce1():
    mock_of_sauce1 = Mock()
    mock_of_sauce1.get_name.return_value = Burger1.sauce_name
    mock_of_sauce1.get_price.return_value = Burger1.sauce_price
    mock_of_sauce1.get_type.return_value = Burger1.sauce_type
    return mock_of_sauce1


@pytest.fixture
def mock_sauce2():
    mock_of_sauce2 = Mock()
    mock_of_sauce2.get_name.return_value = Burger2.sauce_name
    mock_of_sauce2.get_price.return_value = Burger2.sauce_price
    mock_of_sauce2.get_type.return_value = Burger2.sauce_type
    return mock_of_sauce2


@pytest.fixture
def mock_filling1():
    mock_of_filling1 = Mock()
    mock_of_filling1.get_name.return_value = Burger1.filling_name
    mock_of_filling1.get_price.return_value = Burger1.filling_price
    mock_of_filling1.get_type.return_value = Burger1.filling_type
    return mock_of_filling1


@pytest.fixture
def mock_filling2():
    mock_of_filling2 = Mock()
    mock_of_filling2.get_name.return_value = Burger2.filling_name
    mock_of_filling2.get_price.return_value = Burger2.filling_price
    mock_of_filling2.get_type.return_value = Burger2.filling_type
    return mock_of_filling2
