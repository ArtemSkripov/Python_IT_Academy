class BankAccount:

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        if balance < 0:
            raise ValueError('Начальный баланс не может быть отрицательным.')
        self._balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            print('Ошибка! Сумма пополнения должна быть больше нуля.')
            return
        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            print('Ошибка! Сумма снятия должна быть больше нуля.')
            return
        if amount > self._balance:
            print('Ошибка! Недостаточно средств.')
            return
        self._balance -= amount

    @property
    def balance(self) -> float:
        return self._balance

    def __str__(self) -> str:
        return f'Владелец: {self.owner} | Остаток на счету: {self._balance}'


account = BankAccount('Иван', 1000)
print(account.balance)

account.deposit(500)
account.withdraw(2000)
account.withdraw(-100)
account.withdraw(300)

print(account)
