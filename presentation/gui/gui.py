import tkinter
from tkinter import ttk, messagebox
from application.currency_converter import CurrencyConverter
from presentation.localization import message_manager
from presentation.localization.message import InfoMessage
from presentation.localization.message_manager import MessageManager


def window_setup() -> tkinter.Tk:
    window = tkinter.Tk()
    window.title('CurrencyConverter')
    window.geometry('450x350+735+365')

    icon = tkinter.PhotoImage(file='presets/icon.png')
    window.iconphoto(False, icon)
    return window


def gui_input_process(list_of_currences, message_manager: MessageManager) -> (
        tuple[ttk.Combobox, ttk.Combobox, ttk.Entry]):
    base_currency_combobox = ttk.Combobox(values=list_of_currences, state='readonly')
    base_currency_combobox.place(relx=0.1, rely=0.35)

    target_currency_combobox = ttk.Combobox(values=list_of_currences, state='readonly')
    target_currency_combobox.place(relx=0.6, rely=0.35)

    amount_entry = ttk.Entry()
    amount_entry.place(relx=0.1, rely=0.65)

    base_invite_message = message_manager.get_message(InfoMessage.BASE_CURRENCY_INPUT)
    target_invite_message = message_manager.get_message(InfoMessage.TARGET_CURRENCY_INPUT)
    amount_invite_message = message_manager.get_message(InfoMessage.AMOUNT_INPUT)

    base_currency_text = ttk.Label(text=base_invite_message, font=('Arial', 10))
    target_currency_text = ttk.Label(text=target_invite_message, font=('Arial', 10))
    amount_text = ttk.Label(text=amount_invite_message, font=('Arial', 10))
    base_currency_text.place(relx=0.09, rely=0.28)
    target_currency_text.place(relx=0.59, rely=0.28)
    amount_text.place(relx=0.09, rely=0.58)
    return base_currency_combobox, target_currency_combobox, amount_entry


def show_result_info(base_combobox: str, target_combobox: str, amount_entry: float,
                     currency_converter: CurrencyConverter, message_manager):
    base = base_combobox.get()
    target = target_combobox.get()

    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror(message='Amount must be float or integer type')
        exit()

    result_amount = currency_converter.get_target_amount(base, target, amount)

    result_message = message_manager.get_message(InfoMessage.RESULT_MESSAGE)
    result_message = result_message.format_map({
        'target': target,
        'base': base,
        'amount': amount,
        'result_amount': result_amount,

    })

    messagebox.showinfo(
        message=result_message)


def gui_result_process(base_combobox: str, target_combobox: str, amount_entry: float,
                       currency_converter: CurrencyConverter):
    result_button = ttk.Button(text='Конвертировать',
                               command=lambda: show_result_info(base_combobox, target_combobox, amount_entry,
                                                                currency_converter, message_manager))
    result_button.place(relx=0.7, rely=0.65)


def gui(list_of_currences: list, currency_converter: CurrencyConverter, message_manager: MessageManager):
    window = window_setup()
    base, target, amount = gui_input_process(list_of_currences, message_manager)
    gui_result_process(base, target, amount, currency_converter)
    window.mainloop()
