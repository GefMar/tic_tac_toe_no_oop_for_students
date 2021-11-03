import sys


commands_keys = (
    '-u1',
    '-u2',
    '-mode',
)


def help():
    print("help text")


def get_commands():
    result = {}
    if "help" in sys.argv:
        help()
        sys.exit(0)
    else:
        for key in commands_keys:
            if key in sys.argv:
                try:
                    result[key] = sys.argv[sys.argv.index(key) + 1]
                except IndexError:
                    print("Неверный Ввод аргументов")
                    help()
                    sys.exit(1)
    return result
