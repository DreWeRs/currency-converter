from application.currency_converter import CurrencyConverter
from presentation.localization.message import InfoMessage
from presentation.localization.message_manager import MessageManager


def process_input(message_manager: MessageManager) -> tuple[str,str,float]:
    base_invite_message = message_manager.get_message(InfoMessage.BASE_CURRENCY_INPUT)
    target_invite_message = message_manager.get_message(InfoMessage.TARGET_CURRENCY_INPUT)
    amount_invite_message = message_manager.get_message(InfoMessage.AMOUNT_INPUT)
    base = str(input(base_invite_message))
    target = str(input(target_invite_message))
    amount = float(input(amount_invite_message))
    return (base, target, amount)

def process_output(message_manager: MessageManager, amount: float, base: str, target: str, result_amount: float):
    result_message = message_manager.get_message(InfoMessage.RESULT_MESSAGE)
    result_message = result_message.format_map({
        'target': target,
        'base': base,
        'amount': amount,
        'result_amount': result_amount,

    })
    print(result_message)


def cli(message_manager: MessageManager, currency_converter: CurrencyConverter):
    base, target, amount = process_input(message_manager)
    result_amount = currency_converter.get_target_amount(base, target, amount)
    process_output(message_manager, amount, base, target, result_amount)
