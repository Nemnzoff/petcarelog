# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: PetCareLog
import sys

ANSI = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
}

ENABLED = sys.stdout.isatty()


def colorize(text, color):
    if not ENABLED:
        return str(text)
    code = ANSI.get(color)
    if not code:
        return str(text)
    return f"{code}{text}{ANSI['reset']}"


def header(title):
    return f"{colorize('=== ', 'cyan')}{colorize(title, 'white')}{colorize(' ===', 'cyan')}"


def section(title):
    return f"{colorize('>> {title}', 'green')}"


def note(text):
    return colorize(text, "dim")


def ok(text):
    return f"{colorize('\u2713', 'green')} {colorize(text, 'green')}"


def warn(text):
    return f"{colorize('\u26a0', 'yellow')} {colorize(text, 'yellow')}"


def error(text):
    return f"{colorize('\u2717', 'red')} {colorize(text, 'red')}"


def bar(label, value, maximum, width=20):
    ratio = max(0.0, min(1.0, value / maximum)) if maximum else 0.0
    filled = int(round(ratio * width))
    track = colorize("#", "bg_green") * filled + colorize(".", "dim") * (width - filled)
    return f"{colorize(label, 'cyan'):<18} [{track}] {value}/{maximum}"


def palette():
    return [
        ("title", "cyan", "white"),
        ("heading", "green"),
        ("info", "dim"),
        ("success", "green"),
        ("warning", "yellow"),
        ("failure", "red"),
        ("divider", "cyan"),
        ("track", "bg_green"),
        ("track_empty", "dim"),
    ]
