from utils import format_date, mask_card_number, mask_account_number, load_requisites
from operator import itemgetter


def main(operations):
    # Сортируем операции по дате в убывающем порядке
    sorted_operations = sorted(operations, key=itemgetter('date'), reverse=True)

    # Выводим последние 5 операций
    for operation in sorted_operations[:5]:
        print(format_date(operation['date']), operation.get('description', 'Описание отсутствует'))
        print(mask_card_number(operation.get('from', 'Номер карты отсутствует')), "->",
              mask_account_number(operation.get('to', 'Номер счета отсутствует')))
        amount = operation.get('operationAmount', {}).get('amount', 'Сумма отсутствует')
        currency = operation.get('operationAmount', {}).get('currency', {}).get('name', 'Валюта отсутствует')
        print(f"{amount} {currency}\n")


if __name__ == "__main__":
    operations_data = load_requisites()
    main(operations_data)
