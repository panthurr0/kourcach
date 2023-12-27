from datetime import datetime
from src.utils import get_sorted_requisites

requisites = dict(get_sorted_requisites())


class Operation:
    def __init__(self, requisites):
        self.id = requisites['id']
        self.state = requisites['state']
        self.date = datetime.strptime(requisites['date'], "%Y-%m-%dT%H:%M:%S.%f")
        self.operation_amount = {
            'amount': float(requisites['operationAmount']['amount']),
            'currency': {
                'name': requisites['operationAmount']['currency']['name'],
                'code': requisites['operationAmount']['currency']['code']
            }
        }
        self.description = requisites['description']
        self.from_account = requisites['from']
        self.to_account = requisites['to']

    def get_formatted_date(self, format="%d.%m.%Y"):
        return self.date.strftime(format)

    def stars_in_card(self):
        parts = self.from_account.split()
        number = parts[-1]
        if self.from_account.lower().startswith('счет'):
            hided_number = f"**{number[-4:]}"
        else:
            hided_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
        parts[-1] = hided_number
        return ' '.join(parts)

    def stars_in_account(self):
        s = self.to_account
        s_list = list(s)
        s_list[:-4] = "**"
        with_stars = ''.join(s_list)
        return with_stars

# data = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
#         'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#         'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}
#
# transaction = Operation(data)
#
# print(f"ID: {transaction.id}")
# print(f"State: {transaction.state}")
# print(f"Date: {transaction.get_formatted_date()}")
# print(f"Operation Amount: {transaction.operation_amount['amount']} {transaction.operation_amount['currency']['name']}")
# print(f"Description: {transaction.description}")
# print(f"From Account: {transaction.stars_in_card()}")
# print(f"To Account: {transaction.stars_in_account()}")

transaction = Operation(get_sorted_requisites())

print(transaction.id)