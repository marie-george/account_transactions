from packages.json_export import get_bank_data
from datetime import date

bank_data = get_bank_data()


def is_executed():
    bank_data_executed = []
    for i in bank_data:
        if "state" not in i:
            continue
        if i['state'] == "EXECUTED":
            bank_data_executed.append(i)
    return bank_data_executed


def date_sorted():
    bank_data_executed = is_executed()
    for i in bank_data_executed:
        i["date"] = i["date"][:10]
        i["date"] = date.fromisoformat(i["date"])
    bank_data_executed = sorted(bank_data_executed, key=lambda i: i['date'], reverse=True)
    return bank_data_executed


def is_from_absent():
    bank_data_executed = date_sorted()
    for i in bank_data_executed:
        if "from" not in i:
            i["from"] = "Данные отсутствуют"
    return bank_data_executed


def first_five_transactions():
    bank_data_executed = is_from_absent()
    bank_data_short = bank_data_executed[0:5]
    return bank_data_short
