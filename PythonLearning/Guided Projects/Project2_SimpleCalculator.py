#Very simple very easy four function calculator in python to help understand
#Arithmetic and using if, else, and else if statements in python. Also threw in a loop and a function.
# The reason for the loop and the function is to exception handle and challenge my beginner knowledge
#Please note that I have not yet learned loops or functions in python.
#Project 2.
response = None  ##Sets a blank response variable for user input used later in the code.
operand = None   ## Same thing as the response variable but for the mathematical operation.
def ask():  ##Function used to determine which operation a user wants to use.
    operation = input("Please enter a mathematical operation (+ | - | * | /): \n")
    return operation



while True: ##Loop to run through it all, calls function ask() then uses that input if its valid.
    operand = ask()
    if operand not in ("+", "-", "*", "/"):
       print("This is not a valid mathematical operation in a four function calculator. \n")
       continue

    response = input(f"Are you sure want to select {operand} as your operator? Y/N: \n")
    response = response.upper()
    if response == "Y":
        break
    elif response == "N":
        continue
    elif response not in ("N", "Y"):
        while True:
            print("This is not Y/N. Please enter a valid input! \n")
            response = input(f"Are you sure want to select {operand} as your operator? Y/N: \n")
            if response == "Y":
                break
            elif response == "N":
                break

number1 = int(input("Select your first number for the operation: "))
number2 = int(input("Select your second number for the operation: "))
result=0

if operand == "+":
    result = number2 + number1
elif operand == "-":
    result = number1 - number2
elif operand == "*":
    result = number2 * number1
elif operand == "/":
    result = (number1 / number2)
print("\n")
print(f"Your result is {result}.")
print("\n")
print("Thank you, please consider using our calculator again.")

#As I wanted to learn how to navigate some troubles that could arise with some user input. This project became
#slightly more complex than I intended to, but after alot of thought and trial and error, this is the finished product.
#I have familiarity with nested loops from Java, but I did not think that id be using them this soon in python lol 😂

#‼️If project 2 is to complicated please look at project 3 and 4 for more simpler implementations of if statements.

#End of Project 2.