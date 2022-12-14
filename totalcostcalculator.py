# This script will calculate the total cost of a shopping trip
# by adding the prices of all the items in the user's shopping cart

# First, create an empty list to store the prices of the items in the cart
shopping_cart = []

# Ask the user for the price of each item and append it to the shopping_cart list
while True:
    price = float(input("Enter the price of the item (enter 0 to finish): "))
    if price == 0:
        break
    shopping_cart.append(price)

# Calculate the total cost of the shopping trip by summing the prices in the shopping_cart list
total_cost = sum(shopping_cart)

# Print the total cost of the shopping trip
print("The total cost of your shopping trip is: ", total_cost)
