# ALAB 356.3 — Output Logs

Full terminal transcripts for both scripts, captured with `python3 <file>.py`.

## bank_account.py

```
$ python3 bank_account.py
Account 1001 (Alice Smith): $100.00
After deposit of $50: Account 1001 (Alice Smith): $150.00
Error: Deposit amount must be positive.
After withdrawal of $30: Account 1001 (Alice Smith): $120.00
Error: Insufficient funds for this withdrawal.
```

Walkthrough:

1. `BankAccount("1001", "Alice Smith", 100)` — starting balance $100.
2. `deposit(50)` — balance goes to $150.
3. `deposit(-10)` — rejected; `ValueError` caught and printed.
4. `withdraw(30)` — balance goes to $120.
5. `withdraw(1000)` — rejected as an overdraft; `ValueError` caught and printed.

## savings_account.py

```
$ python3 savings_account.py
Account 2002 (Bob Jones): $1000.00, interest rate: 5.00%
After deposit of $200: Account 2002 (Bob Jones): $1200.00, interest rate: 5.00%
Interest applied: $60.00
After interest: Account 2002 (Bob Jones): $1260.00, interest rate: 5.00%
Error: Insufficient funds for this withdrawal.
```

Walkthrough:

1. `SavingsAccount("2002", "Bob Jones", 1000, 0.05)` — starting balance $1000,
   5% rate. `__str__` shows the inherited balance line plus the rate.
2. `deposit(200)` — inherited from `BankAccount` unchanged; balance goes to
   $1200.
3. `apply_interest()` — 5% of $1200 is $60; balance goes to $1260.
4. `withdraw(5000)` — inherited `withdraw()` rejects the overdraft with the
   same `ValueError` message `BankAccount` raises.

Note `bank_account.py` guards its own demo with
`if __name__ == "__main__":`, so importing `BankAccount` into
`savings_account.py` does not print Task 1's output a second time.
