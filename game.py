import random
from random import randint


def game_screen(screen_cells: list[list[list[str]]]) -> None:
    print(f'---------------------')
    print(f'{screen_cells[0][0]}|{screen_cells[0][1]}|{screen_cells[0][2]}|')
    print(f'---------------------')
    print(f'{screen_cells[1][0]}|{screen_cells[1][1]}|{screen_cells[1][2]}|')
    print(f'---------------------')
    print(f'{screen_cells[2][0]}|{screen_cells[2][1]}|{screen_cells[2][2]}|')


def random_choise_first_player() -> int:
    first_player = randint(0, 1)
    return first_player


def check_winner(computers_cells: list[int], players_cells: list[int],
                 game: bool) -> None:
    #Пока не получилось#
    win_ranges = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]
    if sorted(players_cells) in win_ranges:
        print('Вы выиграли')
        game is False
    elif sorted(computers_cells) in win_ranges:
        print('Компьютер выиграл')
        game is False
    else:
        pass


def check_coordinates_for_input(x: int, y: int, empty_cells: list[list[int]]
                                ) -> bool:
    if x < 3 and x >= 0:
        return True
    elif y < 3 and y >= 0:
        return True
    elif [x, y] in empty_cells:
        return True
    else:
        return False


def remove_filled_cells_from_empty(empty_cells: list[list[int]], a: int,
                                   b: int, game: bool
                                   ) -> list[list[int]] | str | bool:
    if len(empty_cells) > 0:
        try:
            empty_cells.remove([a, b])
            return empty_cells
        except ValueError:
            print(f"Эти ячейки не пустые")
    else:
        return game is False


def players_coord(empty_cells: list[list[int]]) -> tuple[int, int]: 
    try:
        x, y = map(int, input('Введите x, y через пробел от 0 до 2х ').split())
        if type(x) != int or type(y) != int:
            print('Вы ввели буквы, а нужно цифры')
        elif check_coordinates_for_input(x, y, empty_cells) is False:
            print('Введены некорректные коoрдинаты ячейки')
        else:
            return x, y
    except ValueError:
        print("Не ввели значение")


def computers_coord(empty_cells: list[list[int]], game: bool
                    ) -> tuple[int, int] | bool:
    if len(empty_cells) > 0:
        x_, y_ = random.choice(empty_cells)
        return x_, y_
    else:
        game is False


def players_pass(empty_cells: list[list[int]],
                 screen_cells: list[list[list[str]]], yours_figure: str,
                 players_cells: list[int], game: bool) -> None:
    print('Игрок ходит')
    try:
        x, y = players_coord(empty_cells)
        screen_cells[x][y] = [yours_figure]
        game_screen(screen_cells)
        remove_filled_cells_from_empty(empty_cells, x, y, game)
        print(f'Остались пустые ячейки {empty_cells}')
        players_cells.extend([[x, y]])
        if len(empty_cells) == 0:
            game is False
    except TypeError:
        game is False


def computers_pass(empty_cells: list[list[int]],
                   screen_cells: list[list[list[str]]],
                   computers_figure: str, computers_cells: list[int], 
                   game: bool) -> None:
    print('Компьютер ходит')
    if computers_coord(empty_cells, game) is False:
        print("Не осталось пустых клеток")
        game is False
    else:
        x_, y_ = computers_coord(empty_cells, game)
        screen_cells[x_][y_] = [computers_figure]
        game_screen(screen_cells)
        remove_filled_cells_from_empty(empty_cells, x_, y_, game)
        print(f'Остались пустые ячейки {empty_cells}')
        computers_cells.extend([[x_, y_]])


def main() -> None:

    screen_cells = [
        [[" "], [" "], [" "]],
        [[" "], [" "], [" "]],
        [[" "], [" "], [" "]]
    ]

    empty_cells = [
        [0, 0], [0, 1], [0, 2],
        [1, 0], [1, 1], [1, 2],
        [2, 0], [2, 1], [2, 2]
    ]

    players_cells: list[int] = []
    computers_cells: list[int] = []

    game_screen(screen_cells)
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
            players_pass(empty_cells, screen_cells, yours_figure,
                         players_cells, game)
            if game is False:
                break
            print(f'{yours_figure} в ячейках {players_cells}')
            if len(players_cells) >= 3:
                check_winner(players_cells, computers_cells, game)
                if game is False:
                    break

            computers_pass(empty_cells, screen_cells, computers_figure,
                           computers_cells, game)
            if game is False:
                break
            print(f'{computers_figure} в ячейках {computers_cells}')
            if len(computers_cells) >= 3:
                check_winner(players_cells, computers_cells, game)
                if game is False:
                    break
        else:
            computers_pass(empty_cells, screen_cells, computers_figure,
                           computers_cells, game)
            if game is False:
                break
            print(f'{computers_figure} в ячейках {computers_cells}')
            if len(computers_cells) >= 3:
                check_winner(players_cells, computers_cells, game)
                if game is False:
                    break

            players_pass(empty_cells, screen_cells, yours_figure,
                         players_cells, game)
            if game is False:
                break
            print(f'{yours_figure} в ячейках {players_cells}')
            if len(players_cells) >= 3:
                check_winner(players_cells, computers_cells, game)
                if game is False:
                    break

    print('Игра окончена')


if __name__ == "__main__":
    main()