menu = {"Popcorn": 1.00, "Hot-dog": 2.00, "Giant Pretzel": 2.00,"Pizza": 3.00 ,"Soda": 1.00, "Bottled Water":1.00}
cart = []
total = 0
print("Welcome to our concession stand, below you can see our menu.")
print("-------------------------MENU---------------------------")
for item, price in menu.items():
    print(f"{item} - ${price:.2f}")
print("-------------------------MENU-END------------------------")

while True:
    response = input("What can we get you (Q to quit)? ")
    if response.upper() == "Q":
        break
    elif menu.get(response) is not None:
        cart.append(response)

for i in cart:
    total += menu.get(i)

print("-------------------------TOTAL BELOW------------------------")
print(f"Your total is ${total:.2f}")


print("---------------------RECEIPT BELOW------------------------")
for item, price in menu.items():
    print(f"{item} - ${price:.2f}")
print(f"You've spent ${total} at the concession stand. Thank you!")
print("-------------------------THANKS FOR SHOPPING------------------------")





