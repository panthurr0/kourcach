import json


def load_requisites():
    with open('../operations.json') as file:
        requisites_data = json.load(file)
    executed_requisites = []

    for i in requisites_data:
        if i.get('state') == "EXECUTED":
            executed_requisites.append(i)

    return executed_requisites


def load_data():
    pass


def sorted_data():
    pass


def stars_in_card():
    pass


def stars_in_bank():
    pass


print(load_requisites())
