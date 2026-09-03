foods = []
prices = []
total = 0

while True:
    food = str(input("Enter an item to buy (q to quit or advance) "))
    if food.lower() == "q":
        break
    price = float(input("Enter the price for this item... $"))
    prices.append(round(price,2))
    foods.append(food)
print("----------YOUR CART BELOW-----------")
print(foods)
print("---------YOUR COST PER ITEM BELOW-------------")

for i,k in zip(foods,prices):  #zip() is a built-in Python function that lets you loop over multiple lists (or collections) at the same time by pairing their elements together.
    print(f"Your cost for {i} is ${k}.")
    total += k
print("---------YOUR TOTAL BELOW----------")
print(f"Your total is ${total}.")
