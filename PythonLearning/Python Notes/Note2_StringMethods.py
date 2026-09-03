# len() Will give you the length of a string, pretty simple. Does not need a calling object.
ex1 = "Length"
print(len(ex1))

#.find() Will find a given character, and only finds the first occurrence
location = ex1.find("g")
print(location)

#.rfind() Means reverse find, and it will find the last occurrence of a character.
#Note that if python cannot find a character in the string, then it will return -1.
#Both find and rfind need a calling object.
ex2 = "OPEN OPERATION"
location = ex2.rfind("O")
print(location)

#The .capitalize() method will capitalize the first letter in a string. Needs a calling object.
ex3 = "this isnt capitalized."
location = ex3.capitalize()
print(location)

#The .upper() method will capitalize the whole string. Needs a calling object.
location = ex3.upper()
print(location)

#The .lower() method will make the entire string lowercase. Needs a calling object.
location = ex3.lower()
print(location)

#The .isdigit() method will check to see if the string contains only digits, boolean value. Needs a calling object.
#I'll demonstrate by turning a string of numbers into an integer.
numbers = "121344553"
if numbers.isdigit():
    numbers = int(numbers)

print(type(numbers))
#If ran, it will output that the original string of numbers is now a class of integers.

#The .isalpha() method will return a boolean to see if the calling object contains only alphabetical characters.
#Only works on strings.
result = (str(numbers)).isalpha()
print(result)

#The .count() method will return how many of the referenced object and contained in a string.
phonenumber = "111-111-1111"
print(phonenumber.count("-"))

#The .replace(?,?) method takes two parameters, first what you want to replace in a string, and what to replace it with.
phonenumber = phonenumber.replace("-", ".")
print(phonenumber)

#To see more string methods do print(help(str))




