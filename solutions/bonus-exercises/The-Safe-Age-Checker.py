#Scenario: Safe Age Checker
#Your app requires users to enter their age. Because users sometimes type letters instead of numbers, you need to prevent the program from crashing using a try-except block.
#Goal: Use a try-except block to catch a standard error and prevent a program from crashing.
#Your Mission
#Write an age-verification program that safely handles messy user inputs.
#Inside the try block, attempt to convert the user_input string into an integer using int().
#If the conversion is successful, print "Success! Your age is: " followed by the number.
#If the user typed letters instead of numbers, Python will throw a ValueError. Use an except ValueError: block to catch this and print a friendly message: "Error: That is not a valid number!".


user_input = input("Please enter your age: ")

# input() always hands back a string, so it has to be converted before it can
# be used as a number. int() raises ValueError on anything that is not a whole
# number, and catching that here is what stops the program from crashing.
try:
    age = int(user_input)
    print("Success! Your age is: " + str(age))
except ValueError:
    print("Error: That is not a valid number!")
