from enum import Enum, auto


class Message(Enum):
    ...

class InfoMessage(Message):
    BASE_CURRENCY_INPUT = auto()
    TARGET_CURRENCY_INPUT = auto()
    AMOUNT_INPUT = auto()
    RESULT_MESSAGE = auto()


class ErrorMessage(Message):
    INVALID_API = auto()
    RATE_ERROR = auto()
    AMOUNT_TYPE_ERROR = auto()
