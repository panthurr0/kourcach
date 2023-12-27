import json
from datetime import datetime


def load_requisites():
    """
    список EXECUTED реквизитов
    """
    with open('../operations.json') as file:
        requisites_data = json.load(file)
    executed_requisites = []

    for i in requisites_data:
        if i.get('state') == "EXECUTED":
            executed_requisites.append(i)

    return executed_requisites


def format_date(date_str):
    """
    Функция для форматирования даты из строки
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")


def mask_card_number(card_number: str) -> str:
    """
    Функция для замаскирования номера карты
    """
    parts = card_number.split()
    number = parts[-1]
    if card_number.lower().startswith('счет'):
        hided_number = f"**{number[-4:]}"
    elif card_number.lower().startswith('номер'):
        hided_number = f"отсутствует"
    else:
        hided_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    parts[-1] = hided_number
    return ' '.join(parts)


def mask_account_number(account_number):
    """
    Функция выводит замаскированный номер счёта
    """
    masked_number = "**" + account_number[-4:]
    return masked_number
