from tic_tac.game import validate_players_coord, check_winner, remove_filled_cells_from_empty, check_coordinates_for_input, choice_computers_coordinates, ParseError
import pytest


def test__validate_players_coor__players_input_parsed():
    empty_cells = [(0, 1), (0, 2)]
    assert validate_players_coord('0 1', empty_cells) == (0, 1)


def test__validate_players_input_failed():
    empty_cells = [[0, 1], [0, 2]]
    with pytest.raises(ParseError) as error:
        validate_players_coord('x 1', empty_cells)
        assert str(error.value) == "Не ввели значение"


def test__check_winner__computer_win():
    computers_cells = {(1, 1), (0, 0), (1, 2), (0, 1), (0, 2)}
    players_cells = {(1, 0), (2, 1), (2, 2)}
    game = True
    game = check_winner(computers_cells, players_cells)

    assert game is False


def test__check_winner__player_win():
    computers_cells = {(1, 1), (0, 0), (1, 2), (0, 1)}
    players_cells = {(2, 1), (2, 0), (2, 2)}
    game = True
    game = check_winner(computers_cells, players_cells)

    assert game is False


def test__check_winner__nobody_win():
    computers_cells = {(1, 1), (0, 0), (1, 2), (0, 1)} 
    players_cells = {(2, 0), (2, 1), (0, 2)}
    game = True
    game = check_winner(computers_cells, players_cells)

    assert game is True

def test__remove_filled_cells_from_empty__success():
    empty_cells = [(0, 0), (0, 1),
                   (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    x = 0
    y = 0

    empty_cells_new = [
        (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2)
    ]

    assert remove_filled_cells_from_empty(empty_cells, x, y) == empty_cells_new


def test__remove_filled_cells_from_empty__failed():
    empty_cells = []
    x = 0
    y = 0
    with pytest.raises(ValueError) as error:
        remove_filled_cells_from_empty(empty_cells, x, y)
        assert str(error.value) == "Нет пустых ячеек"


def test__check_coordinates_for_input__correct_input():
    empty_cells = [(1, 1)]
    x = 1
    y = 1
    assert check_coordinates_for_input(empty_cells, x, y) is True


def test__check_coordinates_for_input__input_out_of_scope():
    empty_cells = [(1, 1), (2, 2)]
    x = 3
    y = 4
    assert check_coordinates_for_input(empty_cells, x, y) is False


def test__check_coordinates_for_input__input_out_of_empty_cells():
    empty_cells = [(1, 1), (2, 2)]
    x = 0
    y = 0
    assert check_coordinates_for_input(empty_cells, x, y) is False


def test__choice_computers_coordinates__():
    empty_cells = [(1, 1)]
    assert choice_computers_coordinates(empty_cells) == (1, 1)


