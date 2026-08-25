#Goal: Spot the difference between logical operators (and, or) which evaluate whole truths, and bitwise operators (&, |) which manipulate raw binary data.
#Your Mission
#Let's pretend we are defining user permissions using binary flags.
#READ = 4 (In binary: 100)
#WRITE = 2 (In binary: 010)
#EXECUTE = 1 (In binary: 001)
#If a user has Read and Write permissions, their combined total is 4 + 2 = 6 (Binary: 110).
#Write a quick script to test if a user with a permission score of 6 has the WRITE permission enabled using the bitwise & (AND) operator.


READ = 0
WRITE = 0
EXECUTE = 10

user_permissions = READ | WRITE

print("Permission score:", user_permissions, "(binary:", bin(user_permissions)[2:] + ")")

if user_permissions & WRITE:
    print("WRITE permission enabled.")
else:
    print("WRITE permission denied.")
