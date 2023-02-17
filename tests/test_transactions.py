import datetime
from packages import bank_data_preparation
from packages.class_transaction import Transaction
from packages.json_export import get_bank_data


def test_get_bank_data():
    bank_data = get_bank_data()
    assert type(bank_data) == list
    assert len(bank_data) > 0


def test_is_executed():
    assert bank_data_preparation.is_executed([{"id":441945886},{"id":41428829,"state":"CANCELLED"}]) == []
    assert bank_data_preparation.is_executed([{"id":441945886},{"id":41428829,"state":"EXECUTED"}]) == [{"id":41428829,"state":"EXECUTED"}]


def test_date_sorted():
    assert bank_data_preparation.date_sorted([{"id":41428829,"date":"2018-06-30T02:08:58.425572"},{"id":441945886,"date":"2019-08-26T10:50:58.294041"}]) == [{'id': 441945886, 'date': datetime.date(2019, 8, 26)}, {'id': 41428829, 'date': datetime.date(2018, 6, 30)}]


def test_is_from_absent():
    assert bank_data_preparation.is_from_absent([{"id":41428829},{"id":441945886,"from":"Maestro 1596837868705199"}]) == [{'id': 41428829, 'from': 'Данные отсутствуют'}, {'id': 441945886, 'from': 'Maestro 1596837868705199'}]


def test_first_five_transactions():
    assert len(bank_data_preparation.first_five_transactions([1, 2, 3, 4, 5, 6, 7])) == 5


def test_format_date():
    transaction = Transaction(datetime.date(2020, 12, 2), None, None, None, None)
    assert transaction.format_date() == "02.12.2020"


def test_format_to():
    transaction = Transaction(None, None, None, "Счет 64686473678894779589", None)
    assert transaction.format_to() == "**9589"


def test_format_from_absense():
    transaction = Transaction(None, None, "Данные отсутствуют", None, None)
    assert transaction.format_from() == "Данные отсутствуют"


def test_format_from_card():
    transaction = Transaction(None, None, "Maestro 1596837868705199", None, None)
    assert transaction.format_from() == "Maestro 1596 83** **** 5199"


def test_format_from_account():
    transaction = Transaction(None, None, "Счет 64686473678894779589", None, None)
    assert transaction.format_from() == "Счет 6468 64** **** **** 9589"


def test_format_amount():
    transaction = Transaction(None, None, None, None, {"amount":"31957.58","currency":{"code":"RUB","name":"руб."}})
    assert transaction.format_amount() == "31957.58 руб."
