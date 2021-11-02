from src.board import get_board
from src.game import game_init, game_cycle, game_end


def main():
    game_vars = game_init()
    end_result = True
    while end_result:
        result_game = game_cycle(**game_vars)
        end_result = game_end(*result_game, game_id=game_vars["game_num"], game_iter_num=game_vars["game_iter_num"])
        if end_result:
            game_vars["board"] = get_board(3)
            game_vars["game_iter_num"] += 1


if __name__ == '__main__':
    main()
