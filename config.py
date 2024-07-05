import os
from dataclasses import dataclass
from types import MappingProxyType
from presentation.localization.message_manager import Messages
from presentation.localization.message import InfoMessage
import tomllib
import typing

CONFIG_PATH = 'config/config.toml'
CONFIG_OPTIONS: MappingProxyType[InfoMessage, str] = MappingProxyType({
    InfoMessage.RESULT_MESSAGE: 'result-message',
    InfoMessage.BASE_CURRENCY_INPUT: 'base-currency-input',
    InfoMessage.TARGET_CURRENCY_INPUT: 'target-currency-input',
    InfoMessage.AMOUNT_INPUT: 'amount-input',

})
Config: typing.TypeAlias = dict[str, str]


@dataclass
class RateAPIConfig:
    base_url: str
    api_key: str

    def get_url(self) -> str:
        return self.base_url.format_map({
            'key': self.api_key
        })


@dataclass
class InfoMessages:
    messages: dict[InfoMessage, str]

    def get_message(self, message: InfoMessage) -> str:
        return self.messages.get(message)


def load_toml() -> Config:
    config_path = os.getenv('CONFIG_PATH')
    with open(config_path, 'rb') as f:
        return tomllib.load(f)


def load_rate_api_config(raw_config: Config) -> RateAPIConfig:
    api = raw_config['api']
    url = api['url']
    api_key = os.getenv('API_KEY')
    return RateAPIConfig(url, api_key)


def load_messages(raw_config: Config) -> Messages:
    info_messages = raw_config.get('messages')
    error_message = raw_config.get('errors')
    all_messages = info_messages | error_message
    messages = {code: all_messages[message_key] for code, message_key in CONFIG_OPTIONS.items()}
    return messages


def load_currencies_list(raw_config: Config) -> list:
    currencies = raw_config.get('currencies')
    list_of_currencies = currencies.get('list-of-currencies')
    return list_of_currencies
