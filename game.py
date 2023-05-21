import random
from random import randint


def draw_game_screen(screen_cells: list[list[str]]) -> None:
    print('----------')
    print(f'{screen_cells[0][0]}|{screen_cells[0][1]}|{screen_cells[0][2]}|')
    print('----------')
    print(f'{screen_cells[1][0]}|{screen_cells[1][1]}|{screen_cells[1][2]}|')
    print('----------')
    print(f'{screen_cells[2][0]}|{screen_cells[2][1]}|{screen_cells[2][2]}|')


def random_choise_first_player() -> int:
    first_player = randint(0, 1)
    return first_player


def check_winner(computers_cells: set[tuple[int, int]], players_cells: set[
                tuple[int, int]]) -> bool:
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


def check_coordinates_for_input(empty_cells: list[tuple[int, int]
                                                  ], x: int, y: int,) -> bool:
    # не работает
    if any(isinstance((x, y), tuple) for (x, y) in empty_cells):
        return True
    else:
        return False


def remove_filled_cells_from_empty(empty_cells: list[tuple[int, int]], x: int,
                                   y: int) -> list[tuple[int, int]]:
    try:
        empty_cells.remove((x, y))
    except ParseError as error:
        print(str(error))
    return empty_cells


class AppError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)
        self.msg = msg


class ParseError(AppError):
    def __init__(self, msg: str, cmd: str) -> None:
        super().__init__(msg)
        self.cmd = cmd


def take_players_coord(empty_cells: list[tuple[int, int]]) -> tuple[int, int]:
    line = input('Введите x, y через пробел от 0 до 2х ')
    x = None
    y = None
    while x is not None and y is not None:
        try:
            x, y = validate_players_coord(line, empty_cells)
        except ParseError as error:
            print(str(error))
    return x, y


def validate_players_coord(line: str, empty_cells: list[tuple[
        int, int]]) -> tuple[int, int]:
    try:
        x, y = map(int, line.split())
        if check_coordinates_for_input(empty_cells, x, y) is False:
            raise ValueError('Введены некорректные коoрдинаты ячейки')
        return x, y
    except ValueError as error:
        raise ValueError("Не ввели значение") from error


def choice_computers_coordinates(empty_cells: list[tuple[
        int, int]]) -> tuple[int, int]:
    try:
        x, y = random.choice(empty_cells)
        return x, y
    except ValueError as error:
        raise ValueError("Нет пустых ячеек") from error


def player_pass(empty_cells: list[tuple[int, int]], screen_cells: list[list
                [str]], yours_figure: str, players_cells: set[tuple[
                    int, int]]) -> bool:
    print('Игрок ходит')
    x, y = take_players_coord(empty_cells)
    screen_cells[x][y] = yours_figure
    draw_game_screen(screen_cells)
    remove_filled_cells_from_empty(empty_cells, x, y)
    players_cells.add((x, y))
    return len(empty_cells) != 0


def computer_pass(empty_cells: list[tuple[int, int]], screen_cells: list[
                    list[str]], computers_figure: str, computers_cells: set[
                        tuple[int, int]]) -> bool:
    print('Компьютер ходит')
    x, y = choice_computers_coordinates(empty_cells)
    screen_cells[x][y] = computers_figure
    draw_game_screen(screen_cells)
    remove_filled_cells_from_empty(empty_cells, x, y)
    computers_cells.add((x, y))


def main() -> None:

    screen_cells = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    empty_cells = [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2)
    ]

    players_cells: set[tuple[int, int]] = set()
    computers_cells: set[tuple[int, int]] = set()

    draw_game_screen(screen_cells)

    game = True
    if random_choise_first_player() == 1:
        yours_figure = "X"
        computers_figure = "O"
        print("Вы ходите первым")
    else:
        yours_figure = "O"
        computers_figure = "X"
        print("Компьютер ходит первым")

    while game is True:
        if yours_figure == 'X':
            game = player_pass(empty_cells, screen_cells, yours_figure,
                               players_cells)
            if not game:
                break
            print(f'{yours_figure} в ячейках {players_cells}')
            if len(players_cells) >= 3:
                check_winner(players_cells, computers_cells)
                if not game:
                    break

            game = computer_pass(empty_cells, screen_cells, computers_figure, 
                                 computers_cells)
            if not game:
                break
            print(f'{computers_figure} в ячейках {computers_cells}')
            if len(players_cells) >= 3:
                check_winner(players_cells, computers_cells)
                if not game:
                    break
        else:
            game = computer_pass(empty_cells, screen_cells, computers_figure,
                                 computers_cells)
            if not game:
                break
            print(f'{computers_figure} в ячейках {computers_cells}')
            if len(players_cells) >= 3:
                check_winner(players_cells, computers_cells)
                if not game:
                    break

            game = player_pass(empty_cells, screen_cells, yours_figure,
                               players_cells)
            if not game:
                break
            print(f'{yours_figure} в ячейках {players_cells}')
            if len(players_cells) >= 3:
                check_winner(players_cells, computers_cells)
                if not game:
                    break

    print('Игра окончена')


if __name__ == "__main__":
    main()