#Scenario: Simple Discount Calculator
#An online store wants a function to calculate the price of an item after applying a discount.
#Goal: Create a reusable block of code with a default parameter and a returned value.
#Your Mission
#Write a function named calculate_price that calculates the final price of an item after applying a discount.
#The function should take two parameters: original_price and discount_rate.
#Set the discount_rate to have a default value of 0.10 (10%).
#The function should calculate the discount amount, subtract it from the original price, and return the final price.


def calculate_price(original_price, discount_rate=0.10):
    # discount_rate has a default, so it can be left off when the discount is 10%.
    discount_amount = original_price * discount_rate
    final_price = original_price - discount_amount
    return final_price


# Using the default 10%.
print(calculate_price(50))

# Passing a discount rate of my own, 25%.
print(calculate_price(50, 0.25))

# The returned value can be stored and used like any other number.
sale_price = calculate_price(80, 0.5)
print(f"Final price: ${sale_price:.2f}")
