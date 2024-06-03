from presentation.localization.message import Message
from typing import TypeAlias

Messages: TypeAlias = dict[Message, str]


class MessageManager():
    messages: Messages

    def __init__(self, messages: Messages):
        self.messages = messages

    def get_message(self, message_code: Message) -> str | None:
        return self.messages.get(message_code)
