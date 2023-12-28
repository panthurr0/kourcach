import json
from datetime import datetime
from operator import itemgetter
from config import DATA


def load_requisites(data_path):
    """
    список EXECUTED реквизитов
    """
    with open(data_path) as file:
        requisites_data = json.load(file)
    return requisites_data


def executed_files(path):
    file = load_requisites(path)
    executed_requisites = []
    for i in file:
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


def sorted_with_date(operations):
    """
    Сортируем операции по дате в убывающем порядке
    """
    sorted_operations = sorted(operations, key=itemgetter('date'), reverse=True)
    return sorted_operations


def print_requisites():
    operations_data = executed_files(DATA)
    sorted_operations = sorted_with_date(operations_data)

    # Выводим последние 5 операций
    for operation in sorted_operations[:5]:
        print(format_date(operation['date']), operation.get('description', 'Описание отсутствует'))
        print(mask_card_number(operation.get('from', 'Номер карты отсутствует')), "->",
              mask_account_number(operation.get('to', 'Номер счета отсутствует')))
        amount = operation.get('operationAmount', {}).get('amount', 'Сумма отсутствует')
        currency = operation.get('operationAmount', {}).get('currency', {}).get('name', 'Валюта отсутствует')
        print(f"{amount} {currency}\n")
