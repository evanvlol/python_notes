# dictionary = collection {key:value} pairs
#         ordered and changeable, no duplicates.


dictionary = {"USA":"Washington D.C.", "Paris": "France", "Italy":"Rome", "England": "London"}
print(dictionary)

print(dictionary.get("USA"))
print(dictionary.get("Paris"))
print(dictionary.get("Italy"))
print(dictionary.get("England"))

if dictionary.get("USA"):
    print("That capital exists.")
else: print("That capital does not exist")

#Use .get() method to check if a key is within the dictionary.

dictionary.update({"India": "New Delhi"})
print(dictionary)
dictionary.update({"USA": "Atlanta"})
print(dictionary)
dictionary.update({"USA": "Washington D.C"})

#Use .popitem() method to remove the latest item, or an item of your choice.
dictionary.popitem()



#To get all keys within dictionary but not their values, use keys() method.
keys = dictionary.keys()
print(keys)

for key in dictionary.keys():
    print(key)

#To get all values within dictionary, use values() method.

values = dictionary.values()

for value in dictionary.values():
    print(value)

#To get all items use items(0 method.

items = dictionary.items()
print(items) #Returns what appears to resemble a 2d list of tuples.

for key, value in dictionary.items():
    print(f"{key}: {value}")
#Just an advanced way to print the pairs without the extra clutter.



