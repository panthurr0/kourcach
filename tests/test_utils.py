from src.utils import (load_requisites, format_date, mask_card_number,
                       mask_account_number, executed_files)
import json
import pytest
import os
from config import DATA_TEST, DATA_TEST_LIST


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
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
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


@pytest.fixture
def mock_operations_file(tmp_path):
    test_data = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01T10:00:00'},
        {'id': 2, 'state': 'PENDING', 'date': '2023-01-02T12:30:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03T15:45:00'},
    ]

    test_file = tmp_path / 'test_data.json'

    with open(test_file, 'w') as file:
        json.dump(test_data, file)

    return test_file


def test_load_requisites_file_exists(mock_operations_file):
    assert os.path.exists(mock_operations_file)


def test_load_requisites_file_format(mock_operations_file):
    with open(mock_operations_file, 'r') as file:
        try:
            json.load(file)
        except json.JSONDecodeError:
            pytest.fail("Invalid JSON format in the operations file")
