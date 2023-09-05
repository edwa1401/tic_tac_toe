import random
from random import randint
from tic_tac.errors import ParseError


def draw_game_screen(screen_cells: list[list[str]]) -> str:
    screen = '\n'.join(
        ['-------',
         f'{screen_cells[0][0]}|{screen_cells[0][1]}|{screen_cells[0][2]}|',
         '-------',
         f'{screen_cells[1][0]}|{screen_cells[1][1]}|{screen_cells[1][2]}|',
         '-------',
         f'{screen_cells[2][0]}|{screen_cells[2][1]}|{screen_cells[2][2]}|'])
    return screen


def random_choise_first_player() -> int:
    first_player = randint(0, 1)
    return first_player


def check_winner(players_cells: set[tuple[int, int]],
                 computers_cells: set[tuple[int, int]]) -> bool:
    win_ranges = [
        {(0, 0), (0, 1), (0, 2)},
        {(1, 0), (1, 1), (1, 2)},
        {(2, 0), (2, 1), (2, 2)},
        {(0, 0), (1, 0), (2, 0)},
        {(0, 1), (1, 1), (2, 1)},
        {(0, 2), (1, 2), (2, 2)},
        {(0, 0), (1, 1), (2, 2)},
        {(0, 2), (1, 1), (2, 0)}
    ]

    for item in win_ranges:
        if item - computers_cells == set():
            print('Компьютер выиграл')
            return False
        elif item - players_cells == set():
            print('Игрок выиграл')
            return False
    return True


def check_coordinates_for_input(
    empty_cells: list[tuple[int, int]], x: int, y: int,
) -> bool:
    return (x, y) in empty_cells


def remove_filled_cells_from_empty(empty_cells: list[tuple[int, int]], x: int,
                                   y: int) -> list[tuple[int, int]]:
    try:
        empty_cells.remove((x, y))
    except ParseError as error:
        print(str(error))
    return empty_cells


def take_players_coord(empty_cells: list[tuple[int, int]]) -> tuple[int, int]:
    x = None
    y = None
    while x is None and y is None:
        try:
            line = input('Введите x, y через пробел от 0 до 2х ')
            x, y = validate_players_coord(line, empty_cells)
        except (ParseError, EOFError) as error:
            print(str(error))
    return x, y


def validate_players_coord(
    line: str, empty_cells: list[tuple[int, int]],
) -> tuple[int, int]:
    try:
        x, y = map(int, line.split())
    except ValueError as error:
        raise ParseError("Не ввели значение", cmd=line) from error
    
    if check_coordinates_for_input(empty_cells, x, y) is False:
        raise ParseError('Введены некорректные коoрдинаты ячейки', cmd=line)
    
    return x, y


def choice_computers_coordinates(empty_cells: list[tuple[
        int, int]]) -> tuple[int, int]:
    try:
        x, y = random.choice(empty_cells)
        return x, y
    except ValueError as error:
        raise ValueError("Нет пустых ячеек") from error


def player_pass(empty_cells: list[tuple[int, int]],
                screen_cells: list[list[str]],
                yours_figure: str,
                players_cells: set[tuple[int, int]]) -> bool:
    print('Игрок ходит:')
    x, y = take_players_coord(empty_cells)
    screen_cells[x][y] = yours_figure
    print(draw_game_screen(screen_cells))
    remove_filled_cells_from_empty(empty_cells, x, y)
    players_cells.add((x, y))
    return len(empty_cells) != 0


def computer_pass(empty_cells: list[tuple[int, int]],
                  screen_cells: list[list[str]],
                  computers_figure: str,
                  computers_cells: set[tuple[int, int]]) -> bool:
    print('Компьютер ходит:')
    x, y = choice_computers_coordinates(empty_cells)
    screen_cells[x][y] = computers_figure
    print(draw_game_screen(screen_cells))
    remove_filled_cells_from_empty(empty_cells, x, y)
    computers_cells.add((x, y))
    return len(empty_cells) != 0



