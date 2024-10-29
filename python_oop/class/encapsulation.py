class BanckAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
        else:
            return "Invalid amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return "Invalid amount"

    def get_balance(self):
        return self.__balance


account = BanckAccount("Rahul", 1200)
print(account.deposit(500))