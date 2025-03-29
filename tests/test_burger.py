from praktikum.burger import Burger
from conftest import *
import pytest


class TestBurger:

    def test_set_buns(self, mock_bun1):
        burger = Burger()
        burger.set_buns(mock_bun1)
        assert burger.bun == mock_bun1


    @pytest.mark.parametrize('ingredients, removed_ingredient', [[Burger1.sauce_name, Burger1.sauce_name], [Burger2.filling_name, Burger2.filling_name]])
    def test_delete_ingredients(self, ingredients, removed_ingredient, mock_filling1):
        burger = Burger()
        burger.add_ingredient(mock_filling1)
        burger.add_ingredient(ingredients)
        burger.remove_ingredient(1)
        assert removed_ingredient not in burger.ingredients and mock_filling1 in burger.ingredients


    def test_move_ingredients(self, mock_sauce1, mock_filling1):
        burger = Burger()
        burger.add_ingredient(mock_sauce1)
        burger.add_ingredient(mock_filling1)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == mock_filling1 and burger.ingredients[1] == mock_sauce1


    @pytest.mark.parametrize('ingredients, added_ingredient', [[Burger1.sauce_name, Burger1.sauce_name], [Burger1.filling_name, Burger1.filling_name], [Burger1.filling_name, Burger1.filling_name]])
    def test_add_ingredients(self, ingredients, added_ingredient):
        burger = Burger()
        burger.add_ingredient(ingredients)
        assert burger.ingredients == [added_ingredient] and len(burger.ingredients) == 1


    def test_get_price_of_burger(self, mock_bun2, mock_sauce2, mock_filling2):
        burger = Burger()
        burger.set_buns(mock_bun2)
        burger.add_ingredient(mock_sauce2)
        burger.add_ingredient(mock_filling2)
        assert burger.get_price() == Burger2.burger_price
