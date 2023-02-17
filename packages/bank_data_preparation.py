from datetime import date


def is_executed(transactions_list):
    bank_data_executed = []
    for i in transactions_list:
        if "state" not in i:
            continue
        if i['state'] == "EXECUTED":
            bank_data_executed.append(i)
    return bank_data_executed


def date_sorted(transactions_list):
    for i in transactions_list:
        i["date"] = i["date"][:10]
        i["date"] = date.fromisoformat(i["date"])
    bank_data_executed = sorted(transactions_list, key=lambda i: i['date'], reverse=True)
    return bank_data_executed


def is_from_absent(transactions_list):
    for i in transactions_list:
        if "from" not in i:
            i["from"] = "Данные отсутствуют"
    return transactions_list


def first_five_transactions(transactions_list):
    bank_data_short = transactions_list[0:5]
    return bank_data_short
