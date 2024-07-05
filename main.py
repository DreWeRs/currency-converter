from functools import partial
from application.currency_converter import CurrencyConverter, CurrencyGetter
from config import load_rate_api_config, load_toml, load_messages, load_currencies_list
from presentation.gui.gui import gui
from presentation.localization.message_manager import MessageManager
from presentation.cli import cli


def main():
    raw_config = load_toml()
    rate_api_config = load_rate_api_config(raw_config)
    messages = load_messages(raw_config)
    list_of_currencies = load_currencies_list(raw_config)
    message_manager = MessageManager(messages)

    currency_getter = CurrencyGetter(rate_api_config.get_url(), message_manager)
    currency_converter = CurrencyConverter(currency_getter)

    user_interface = {
        'cli': partial(cli, currency_converter, message_manager),
        'gui': partial(gui, list_of_currencies, currency_converter, message_manager)
    }
    available = ', '.join([x for x in user_interface.keys()])
    user_interface_prompt = input(f'Choose interface (available: {available}): ')
    selected_interface = user_interface.get(user_interface_prompt)
    if not selected_interface:
        raise ValueError('Interface not found')
    selected_interface()


if __name__ == main():
    try:
        main()
    except Exception as e:
        print(e)
