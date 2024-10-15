from typing import Literal

terminal_colors = {
    "default": "",
    "gray": "\033[90m",
    "green": "\033[32m",
    "red": "\033[31m",
}
terminal_modifiers = {
    "reset": "\033[0m",
    "bold": "\033[1m",
}

BuildLogTextColor = Literal["default", "gray", "green", "red"]


def log(message, color: BuildLogTextColor = "default", bold: bool = False, *args, **kwargs):
    if color not in terminal_colors:
        raise ValueError(f"Color \"{color}\" must be one of: {', '.join(terminal_colors.keys())}")

    print(f"{terminal_colors[color]}"
          f"{terminal_modifiers['bold'] if bold else ''}"
          f"{message}"
          f"{terminal_modifiers['reset']}",
          *args, **kwargs)
