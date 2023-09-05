from tic_tac.game import (check_winner, computer_pass, draw_game_screen,
                          player_pass, random_choise_first_player)

from tic_tac.errors import AppError


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

    print(draw_game_screen(screen_cells))

    game = True
    if random_choise_first_player() == 1:
        yours_figure = "X"
        computers_figure = "O"
        print("Вы ходите первым, играете Х")
    else:
        yours_figure = "O"
        computers_figure = "X"
        print("Компьютер ходит первым, вы играете О")

    while game is True:
        if yours_figure == 'X':
            game = player_pass(empty_cells, screen_cells, yours_figure,
                               players_cells)
            if len(players_cells) >= 3:
                game = check_winner(players_cells, computers_cells)
                if not game:
                    break
            if not game:
                print('Ничья')
                break

            game = computer_pass(empty_cells, screen_cells, computers_figure,
                                 computers_cells)
            if len(players_cells) >= 3:
                game = check_winner(players_cells, computers_cells)
                if not game:
                    break
            if not game:
                print('Ничья')
                break

        else:
            game = computer_pass(empty_cells, screen_cells, computers_figure,
                                 computers_cells)
            if len(players_cells) >= 3:
                game = check_winner(players_cells, computers_cells)
                if not game:
                    break
            if not game:
                print('Ничья')
                break

            game = player_pass(empty_cells, screen_cells, yours_figure, 
                               players_cells)
            if len(players_cells) >= 3:
                game = check_winner(players_cells, computers_cells)
                if not game:
                    break
            if not game:
                print('Ничья')
                break

    print('Игра окончена')


if __name__ == "__main__":

    try:
        main()
    except AppError as error:
        print(error.msg)
    