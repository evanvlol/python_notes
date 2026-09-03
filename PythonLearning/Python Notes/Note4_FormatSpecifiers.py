#format specifiers = {value:flags} format a value
# based on the flags that are inserted

price1 = 3.133131
price2 = 13013
price3 = 3121
print(f"Price 1 is {price1:.2f}") #Also can use round(variable, decimal place)
print(f"Price 2 is {price2:.2f}")
print(f"Price 3 is {price3:.2f}")


def add(a, b):
    print(a+b)

# The .f flag deals with floating point numbers
# Just inserting a number as the flag makes it that many spaces

print(f"Price 1 is {price1:10}")

#To move it to the left or right you can use < for left and > for right.
#Center align is the ^ symbol.
#If you have any positive values you can use the + flag.
#To lign outputs up evenly just use the ": " flag
#The , flag will add commas based on the place in the number... ex below.
price4 = 1212013001
print(f"Price 4 is {price4:^+10,.2f}") #You can combine specifiers. Order does matter though.



