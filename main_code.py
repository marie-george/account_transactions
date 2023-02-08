from packages.bank_data_preparation import*
from packages.class_transaction import*

bank_data_short = first_five_transactions()

for i in bank_data_short:
    transaction = Transaction(i['date'], i['description'], i['from'], i['to'], i['operationAmount'])
    print(f'{transaction.format_date()} {transaction.descr}\n{transaction.format_from()} -> {transaction.format_to()}\n{transaction.format_amount()}\n')