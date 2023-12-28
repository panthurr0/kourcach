from src.utils import (print_requisites, sorted_with_date, load_requisites, format_date, mask_card_number,
                       mask_account_number, executed_files)
from config import DATA_TEST, DATA_TEST_LIST, DATA


def test_load_requisites():
    data_path = DATA_TEST
    assert load_requisites(data_path) == [
        {
            "id": 801684332,
            "state": "EXECUTED",
            "date": "2019-11-05T12:04:13.781725",
            "operationAmount": {
                "amount": "21344.35",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 77613226829885488381"
        }
    ]


def test_executed_files():
    file = DATA_TEST_LIST
    assert executed_files(file) == [
        {
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {
                "amount": "40701.91",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472"
        }
    ]


def test_sorted_with_date():
    operations_data = executed_files(DATA_TEST_LIST)
    assert sorted_with_date(operations_data) == [
        {
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {
                "amount": "40701.91",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472"
        }
    ]


def test_format_date():
    date_str = '2023-01-01T10:00:00'
    formatted_date = format_date(date_str)
    assert formatted_date == '01.01.2023'


def test_mask_card_number():
    card_number = 'Номер карты 1234 5678 8765 4321'
    masked_number = mask_card_number(card_number)
    assert masked_number == 'Номер карты 1234 5678 8765 отсутствует'


def test_mask_card_number_account():
    card_number = 'Счет **3355'
    masked_number = mask_card_number(card_number)
    assert masked_number == 'Счет **3355'


def test_default_card_bank():
    card_number = 'Visa Gold 7305799447374042'
    masked_number = mask_card_number(card_number)
    assert masked_number == 'Visa Gold 7305 79** **** 4042'


def test_mask_account_number():
    account_number = '1234567890123456'
    masked_number = mask_account_number(account_number)
    assert masked_number == '**3456'


def test_print_requisites():
    operations_data = executed_files(DATA)
    sorted_operations = sorted_with_date(operations_data)

    assert print_requisites(sorted_operations) == '''
    08.12.2019 Открытие вклада
    Номер карты отсутствует -> **5907
    41096.24 USD

    07.12.2019 Перевод организации
    Visa Classic 2842 87** **** 9012 -> **3655
    48150.39 USD

    19.11.2019 Перевод организации
    Maestro 7810 84** **** 5568 -> **2869
    30153.72 руб.

    13.11.2019 Перевод со счета на счет
    Счет **9794 -> **8125
    62814.53 руб.

    05.11.2019 Открытие вклада
    Номер карты отсутствует -> **8381
    21344.35 руб.\n'''

