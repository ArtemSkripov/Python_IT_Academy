class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError('Баланс не может быть отрицательным')
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def _change_balance(self, amount):
        self.__balance += amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Сумма должна быть больше нуля')
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Сумма должна быть больше нуля')
        if amount > self.__balance:
            raise ValueError('Недостаточно средств')
        self.__balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self._interest_rate = interest_rate

    def apply_interest(self):
        self.deposit(self.balance * self._interest_rate)


class CreditAccount(BankAccount):
    def __init__(self, owner, balance=0, credit_limit=1000):
        super().__init__(owner, balance)
        self.__credit_limit = credit_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Сумма должна быть больше нуля')
        if amount > self.balance + self.__credit_limit:
            raise ValueError('Превышен кредитный лимит')
        self._change_balance(-amount)


acc1 = BankAccount('Иван', 1000)
acc1.deposit(500)
acc1.withdraw(200)
print(acc1.balance)

acc1.__balance = 1000000
print(acc1.balance)

acc2 = SavingsAccount('Мария', 2000, 0.1)
acc2.apply_interest()
print(acc2.balance)

acc3 = CreditAccount('Петр', 500, 1000)
acc3.withdraw(1200)
print(acc3.balance)
