# ALAB 356.3 - Task 1: BankAccount base class
# A BankAccount with deposit and withdraw methods that validate their input
# and raise ValueError on a bad amount, plus a __str__ for readable printing.

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for this withdrawal.")
        self.balance -= amount

    def __str__(self):
        return f"Account {self.account_number} ({self.owner}): ${self.balance:.2f}"


# Demonstration. Guarded so that savings_account.py can import BankAccount
# without re-running this script's own output.
if __name__ == "__main__":
    account = BankAccount("1001", "Alice Smith", 100)
    print(account)

    account.deposit(50)
    print("After deposit of $50:", account)

    try:
        account.deposit(-10)
    except ValueError as e:
        print("Error:", e)

    account.withdraw(30)
    print("After withdrawal of $30:", account)

    try:
        account.withdraw(1000)
    except ValueError as e:
        print("Error:", e)
