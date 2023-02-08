class Transaction:
    def __init__(self, date_, descr, from_=None, to_=None, amount=None):
        self.date_ = date_
        self.descr = descr
        self.from_ = from_
        self.to_ = to_
        self.amount = amount

    def format_date(self):
        self.date_ = self.date_.strftime("%d.%m.%Y")
        return self.date_

    def format_to(self):
        split_digits = self.to_[-4:]
        self.to_ = f'**{split_digits}'
        return self.to_

    def format_from(self):
        if self.from_ == "Данные отсутствуют":
            return "Данные отсутствуют"
        if self.from_[0:4] == "Счет":
            first_digits = self.from_[-20:-16]
            second_digits = self.from_[-16:-15]
            last_digits = self.from_[-4:]
            return f'Счет {first_digits} {second_digits}** **** **** {last_digits}'
        else:
            card_type = self.from_[:-17]
            first_digits = self.from_[-16:-12]
            second_digits = self.from_[-12:-10]
            last_digits = self.from_[-4:]
            return f'{card_type} {first_digits} {second_digits}** **** {last_digits}'

    def format_amount(self):
        amount = self.amount['amount']
        currency = self.amount['currency']['name']
        return f'{amount} {currency}'
