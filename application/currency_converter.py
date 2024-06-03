from types import MappingProxyType

import requests

from presentation.localization.message_manager import MessageManager


class CurrencyGetter:
    def __init__(self, url: str, message_manager: MessageManager):
        self.url = url
        self.message_manager = message_manager


    def get_currency_rate(self, base: str, target: str) -> float:
        response = requests.get(self.url + base)

        if response.status_code == 403:
            raise ValueError('incorrect API key')

        data = MappingProxyType(response.json())
        conversion_rates = data.get('conversion_rates')

        if type(conversion_rates) is None:
            raise TypeError('Error when trying to get currency_rates')

        current_rate = conversion_rates.get(target)
        return current_rate


class CurrencyConverter:
    def __init__(self, currency_getter: CurrencyGetter):
        self.currency_getter = currency_getter

    def get_target_amount(self, base: str, target: str, amount: float) -> float:
        return self.currency_getter.get_currency_rate(base, target) * amount

