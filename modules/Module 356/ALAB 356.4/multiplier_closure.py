# ALAB 356.4 - Task 2: Multiplier Closure
# make_multiplier(factor) returns a closure that multiplies its input by
# factor. Each closure remembers its own factor after make_multiplier
# returns.

def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier


# Demonstration
times3 = make_multiplier(3)
times10 = make_multiplier(10)

print("times3(5) =", times3(5))
print("times3(12) =", times3(12))
print("times10(5) =", times10(5))
print("times10(7) =", times10(7))
