def defaultarg(money: float = 1000, savings: float = 100) -> None:
    print(f"You have ${money} in your checking account, and ${savings} account", end = " ")
    print("Goodbye.")

def keywordarg(last: str = "Last name", first: str = "First name", middle: str = "Middle Name"):
    print(f"You are {first} {middle} {last}.")


def main() -> None :
    defaultarg() #Note that you don't need to pass anything as a parameter because you've already set a default argument.
    keywordarg(middle="Bobby", first="Joe", last="Lamilton")
    print(add(1,2,3,4,5,6))
    print_addy("Gates", "Bill", "III", street = "Stewart", city= "Manchester", state="Bosnia", zipcode="Freaky")

def print_addy(*arguments, **kwargs):
    print(type(kwargs))
    for arg in arguments:
        print(f"{arg}", end = " ")
    print()
    for kwarg in kwargs:
        print(f"{kwargs.get(kwarg)}", end = " ")


#Args and Kwargs, Tuples for args, Dictionaries for Kwargs. Keyword arguments btw.
#ex below # Use these when you dont know how many arguments ar being passed
def add(*args):
    print(type(args))
    total = 0
    for arg in args:
        total += arg
    return total


main()







