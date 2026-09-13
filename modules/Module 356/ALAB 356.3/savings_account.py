# ALAB 356.3 - Task 2: SavingsAccount subclass
# SavingsAccount inherits from BankAccount, adds an interest_rate, and can
# grow its own balance with apply_interest(). __str__ is overridden to add
# the rate on top of what BankAccount already prints.

from bank_account import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.0):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest

    def __str__(self):
        return f"{super().__str__()}, interest rate: {self.interest_rate:.2%}"


# Demonstration
savings = SavingsAccount("2002", "Bob Jones", 1000, 0.05)
print(savings)

savings.deposit(200)
print("After deposit of $200:", savings)

interest = savings.apply_interest()
print(f"Interest applied: ${interest:.2f}")
print("After interest:", savings)

try:
    savings.withdraw(5000)
except ValueError as e:
    print("Error:", e)
