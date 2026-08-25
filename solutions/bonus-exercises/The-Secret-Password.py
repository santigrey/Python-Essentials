#Goal: Use a while loop to keep a program running until a specific logical condition is met.
#Your Mission
#Write a program that continuously asks the user to input a password.
#The loop should only stop if the user types "python123" OR if they have guessed incorrectly 3 times (intruder alert!).
#If they get it right, print: "Access granted."
#If they run out of attempts, print: "Account locked. Try again later."


attempts = 0

while attempts < 3:
    password = input("Enter the password: ")
    if password == "python123":
        print("Access granted.")
        break
    attempts += 1
else:
    print("Account locked. Try again later.")
