import json
from typing import NamedTuple


class Style:
    PURPLE = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"


class Emoji:
    FIRE = "\U0001f525"
    RAINBOW = "\U0001f308"
    ALIEN = "\U0001f47d"
    ROBOT = "\U0001f916"
    TOOL = "\U0001f527"
    BULLETPOINT = "\U000025b6"


Expression = NamedTuple("Expression", ["color", "emoji"])


class MessageLevel:
    ERROR = Expression(Style.RED, Emoji.FIRE)
    SUCCESS = Expression(Style.GREEN, Emoji.RAINBOW)
    WARNING = Expression(Style.YELLOW, Emoji.ALIEN)
    INFO = Expression(Style.BLUE, Emoji.ROBOT)
    REMEDY = Expression(Style.PURPLE, Emoji.TOOL)


def print_body(message_level: MessageLevel, content: str, indentation: int = 4):
    """Print a message with a given color (but no emoji) and with an indentation (default 4)."""
    print((indentation * " ") + message_level.color + content + Style.END)


def emote(message_level: MessageLevel, content: str, indentation: int = 2) -> None:
    """Print a message with an emoji and color that corresponds to the message level."""
    print(message_level.emoji + (indentation * " ") + message_level.color + content + Style.END)


def emote_with_pretty_json(message_level: MessageLevel, content: str, json_dict: dict) -> None:
    """Print an emotive text followed by pretty json.

    Prints a message with an emoji and color that corresponds to the message level followed by a
    formatted dictionary.
    """
    emote(message_level, content)
    formatted_str = json.dumps(
        {k: str(v) for k, v in json_dict.items()},
        indent=4,
        sort_keys=True,
    )
    print(message_level.color + formatted_str + Style.END)


def emote_with_header(message_level: MessageLevel, header: str, content: str) -> None:
    """Print a message with a header in bold followed by indented content."""
    print(message_level.emoji + "  " + message_level.color + Style.BOLD + header + Style.END)
    print_body(message_level, content)


def print_list(message_level: MessageLevel, data: list) -> None:
    """Print out a bulletpoint list in the color corresponding to the message level."""
    for element in data:
        print(f"{message_level.color}\t{Emoji.BULLETPOINT}  {element}{Style.END}")


def emote_with_header_and_list(message_level: MessageLevel, header: str, content: str, data: list) -> None:
    """Print a messages with an emoji and color that corresponds to the message level.

    The first line starts with an emoji and is bold.
    The next line is the message, which is followed by a list of data, e.g. data points affected by
    the message.
    """
    emote_with_header(message_level, header, content)
    print_list(message_level, data)


def emote_with_list(message_level: MessageLevel, content: str, data: list) -> None:
    """Print a messages with an emoji and color that corresponds to the message level.

    The message is followed by a list of data, e.g. data points affected by the message.
    """
    emote(message_level, content)
    print_list(message_level, data)
