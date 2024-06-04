'''Write a program collecting details of a pizza order. Assume (in your code) some set of sauces, toppings, and their prices. After collecting all data display a description of the pizza and its price. You can assume that the client, though hungry, always gives valid answers.

In this program you have to use variables. Note that in Python (in constant to many other programming languages) you do not have (in fact you cannot) declare them. Just use them - Pyhon is simple!

Sample output of the program:

Pizzarino Ltd. The best pizza deliveries in this century and galaxy!
Do you want the (T)omato or (M)ayonnaise sauce? T
Do you want onion (Y/N)? Y
Do you want mushrooms (Y/N)? Y
Do you want jalapenos (Y/N)? N
Do you want corn (Y/N)? Y
Do you want black olive (Y/N)? Y
You have ordered a pizza with: tomato sauce, onion, mushrooms, corn, black olive. The price is $12.5.'''


# Pizza details and prices
sauce_price = 2.0
topping_prices = {
    "onion": 1.5,
    "mushrooms": 2.0,
    "jalapenos": 1.8,
    "corn": 1.0,
    "black olive": 1.2
}

# Welcome message
print("Pizzarino Ltd. The best pizza deliveries in this century and galaxy!")

# Collect sauce choice from the user
sauce_choice = input("Do you want the (Tomato or (M)ayonnaise sauce?: ").upper()
sauce_name = "Tomato" if sauce_choice == "T" else "Mayonnaise"

# Initialize toppings list
toppings = []

# Collect topping choices from the user
if input("Do you want onion (Y/N)? ").upper() == "Y":
    toppings.append("onion")
if input("Do you want mushrooms (Y/N)? ").upper() == "Y":
    toppings.append("mushrooms")
if input("Do you want jalapenos (Y/N)? ").upper() == "Y":
    toppings.append("jalapenos")
if input("Do you want corn (Y/N)? ").upper() == "Y":
    toppings.append("corn")
if input("Do you want black olive (Y/N)? ").upper() == "Y":
    toppings.append("black olive")

# Calculate the total price
total_price = sauce_price + sum(topping_prices[topping] for topping in toppings)

# Display the pizza description and total price
print(f"You have ordered a pizza with: {sauce_name} sauce, {', '.join(toppings)}. The price is ${total_price}.")
