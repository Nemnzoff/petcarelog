# === Stage 55: Add a setting to disable colorized output ===
# Project: PetCareLog
DISABLE_COLOR = False


def colorize(text, color):
    if DISABLE_COLOR:
        return text
    return "\033[1;{}m{}\033[0m".format(color, text)


def red(text):
    return colorize(text, "31")


def green(text):
    return colorize(text, "32")


def yellow(text):
    return colorize(text, "33")


def blue(text):
    return colorize(text, "34")


def magenta(text):
    return colorize(text, "35")


def cyan(text):
    return colorize(text, "36")


def white(text):
    return colorize(text, "37")


def bold(text):
    return colorize(text, "1")


def dim(text):
    return colorize(text, "2")


def set_color_enabled(value):
    global DISABLE_COLOR
    DISABLE_COLOR = bool(value)


def print_header(title):
    print(colorize(title, "1;36"))


def print_success(message):
    print(colorize("  " + message, "32"))


def print_warning(message):
    print(colorize("  " + message, "33"))


def print_error(message):
    print(colorize("  " + message, "31"))


def print_info(message):
    print(colorize("  " + message, "37"))


def print_table(headers, rows):
    width = max([len(h) for h in headers] + [len(str(r)) for r in rows])
    line = "  " + "  ".join(h.ljust(width) for h in headers)
    print(colorize(line, "1"))
    for row in rows:
        print("  " + "  ".join(str(c).ljust(width) for c in row))
