from packages.bank_data_preparation import*
from packages.class_transaction import*
from packages.json_export import*


def main():
    bank_data = get_bank_data()
    bank_data = is_executed(bank_data)
    bank_data = date_sorted(bank_data)
    bank_data = is_from_absent(bank_data)
    bank_data = first_five_transactions(bank_data)
    for i in bank_data:
        transaction = Transaction(i['date'], i['description'], i['from'], i['to'], i['operationAmount'])
        print(f'{transaction.format_date()} {transaction.descr}\n{transaction.format_from()} -> {transaction.format_to()}\n{transaction.format_amount()}\n')

main()