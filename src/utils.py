import json
from datetime import datetime
from operator import itemgetter


def format_date(date_str):
    # Функция для форматирования даты из строки
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")


def mask_card_number(card_number):
    # Функция для замаскирования номера карты
    masked_number = card_number[:4] + " XX** **** " + card_number[-4:]
    return masked_number


def mask_account_number(account_number):
    # Функция для замаскирования номера счета
    masked_number = "**" + account_number[-4:]
    return masked_number


def print_recent_operations(operations):
    # Сортируем операции по дате в убывающем порядке
    sorted_operations = sorted(operations, key=itemgetter('date'), reverse=True)

    # Выводим последние 5 операций
    for operation in sorted_operations[:5]:
        print(format_date(operation['date']), operation['description'])
        print(mask_card_number(operation['from']), "->", mask_account_number(operation['to']))
        print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
        print()


# Пример данных из вашего JSON файла
operations_data = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    # Добавьте остальные операции из вашего JSON файла
]

# Выводим результат
print_recent_operations(operations_data)
