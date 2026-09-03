print("Welcome to the compound Interest Calculator. Please note that this calculator will only work if your interest is compounded monthly or yearly.")
print("If at any process you wish to quit, please hit 'Q' on your keyboard")
response = float(input("Please entire the principle amount: "))
principle = response
interest = None
time_compounded = None

def checkQ(response):
    if response == "Q":
        quit()

while not response == 'Q':
    response = str(input("Please entire the interest rate (ex. 5%): "))
    checkQ(response)
    response = response.replace("%","")
    interest = response
    response = str(input("Is this interest compounded monthly or yearly (M/Y)? "))
    checkQ(response)
    time_compounded = response
    break




