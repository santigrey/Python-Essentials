# ALAB 356.3 - Object-Oriented Programming

**Name:** James Sloan
**Course:** Python Essentials (UCI 3052)
**Date:** September 13, 2026

A `BankAccount` base class with validated deposits and withdrawals, and a
`SavingsAccount` subclass that adds an interest rate on top of it.

## Files

| File | Purpose |
| --- | --- |
| `bank_account.py` | Task 1 — `BankAccount` with `deposit()`, `withdraw()`, and `__str__()`. Both `deposit()` and `withdraw()` raise `ValueError` on a bad amount. |
| `savings_account.py` | Task 2 — `SavingsAccount(BankAccount)`, built with `super().__init__()`, adding `interest_rate` and `apply_interest()`. `__str__()` is overridden to add the rate on top of the inherited line. |
| `ALAB-356.3-Canvas-Submission.pdf` | The one-page PDF submitted to Canvas — direct clickable links to each script. |
| `ALAB-356.3-output-logs.md` | Captured terminal transcripts for both scripts. |
| `screenshot-1-bank_account.png`<br>`screenshot-2-savings_account.png` | Terminal screenshots of each script running. |

## How to run

```bash
cd "modules/Module 356/ALAB 356.3"
python3 bank_account.py
python3 savings_account.py
```

Python 3.9 or newer. No third-party packages. Neither script asks for input —
each runs a fixed demonstration.

---

## Example output

### bank_account.py

```
Account 1001 (Alice Smith): $100.00
After deposit of $50: Account 1001 (Alice Smith): $150.00
Error: Deposit amount must be positive.
After withdrawal of $30: Account 1001 (Alice Smith): $120.00
Error: Insufficient funds for this withdrawal.
```

`deposit(-10)` and `withdraw(1000)` both raise `ValueError` — a non-positive
amount and an overdraft, respectively — and both are caught and printed
without stopping the script.

### savings_account.py

```
Account 2002 (Bob Jones): $1000.00, interest rate: 5.00%
After deposit of $200: Account 2002 (Bob Jones): $1200.00, interest rate: 5.00%
Interest applied: $60.00
After interest: Account 2002 (Bob Jones): $1260.00, interest rate: 5.00%
Error: Insufficient funds for this withdrawal.
```

`SavingsAccount` gets `deposit()` and `withdraw()` for free from
`BankAccount` — neither is redefined. `apply_interest()` is new: 5% of
$1200 is $60, added straight to `self.balance`. The final `withdraw(5000)`
proves the inherited validation still applies to the subclass.

Full transcripts are in `ALAB-356.3-output-logs.md`.

---

## Rubric mapping

Rubric taken from the lab text at
`ps-lms.vercel.app/curriculum/netacad/pe2/lab-3/`, which is the page the Canvas
assignment embeds.

| Criterion | Points | Where it is met |
| --- | --- | --- |
| BankAccount Implementation | 20 | `bank_account.py` — `account_number`, `owner`, `balance` set in `__init__`; `deposit()`, `withdraw()`, `__str__()` all present |
| Exception Handling | 10 | `deposit()` rejects amounts ≤ 0; `withdraw()` rejects amounts ≤ 0 and amounts greater than the balance; both raise `ValueError` with a clear message |
| SavingsAccount Subclass | 15 | `savings_account.py` — `SavingsAccount(BankAccount)`, `super().__init__()`, `interest_rate` attribute, `apply_interest()`, `__str__()` overridden to add the rate |
| Testing & Demonstration | 10 | Both scripts create an instance, run normal operations, and trigger an exception on each validated method |
| Code Organization and Style | 5 | Comments in every script, descriptive names, labeled output, this README and the logs |

Task 3 (a custom `InsufficientFundsError`) is marked optional in the lab and
is not part of the 60-point rubric, so it is left out — same call as ALAB
356.2's age validator, which used the standard `ValueError` rather than a
custom exception class.
