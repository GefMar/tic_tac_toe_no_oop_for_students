import os
import datetime
from settings import LOG_FOLDER


SYMBOLS = ("X", "O")
DELIMITER = ';'

COMP_NAMES = [
    "R2D2",
    "C3PO",
    "WALLE",
    "DALEK",
]

USER_TEMPLATE = (
    ("name", lambda name=None, *args, **kwargs: name or input("ВВЕДИТЕ ВАШЕ ИМЯ")),
    ("symbol", lambda symbol, *args, **kwargs: symbol),
    ("steps", lambda *args, **kwargs: list()),
    ("all_steps", lambda *args, **kwargs: set()),
    ("user_type", lambda user_type, *args, **kwargs: user_type),
)

FILE_HANDLERS = {
    "GAME_NUM": os.path.join(LOG_FOLDER, "game_num_inc"),
    "INIT_GAME": os.path.join(LOG_FOLDER, "game_init"),
    "GAME_STEP": os.path.join(LOG_FOLDER, "game_log"),
    "END_GAME": os.path.join(LOG_FOLDER, "end_game"),
}

INIT_ROW_TEMPLATE = {
    "game_id": int,
    "mode": str,
    "x_user_name": str,
    "o_user_name": str,
    "date_start": datetime.datetime.fromisoformat,
}
GAME_LOG_TEMPLATE = ("game_id", "step_date", "user_name", "user_step", "game_iter_num")
