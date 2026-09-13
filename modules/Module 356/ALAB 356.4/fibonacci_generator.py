# ALAB 356.4 - Task 1: Fibonacci Generator
# gen_fibonacci(n) yields the Fibonacci sequence, one number at a time,
# up to the first n numbers.

def gen_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Demonstration
for i, value in enumerate(gen_fibonacci(10), start=1):
    print(f"Fibonacci #{i}: {value}")
