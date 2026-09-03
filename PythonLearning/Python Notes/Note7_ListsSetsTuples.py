#In python, you have lists, sets, and tuples.

# List = [] and this is ordered and changeable. Allows for duplicates.
# Set = {} and this is unordered and unchangeable. But you can add/remove. No duplicates.
# Tuple = () and this is ordered and unchangeable. Allows for duplicates nand is faster.


fruits = ["apple", "orange", "pineapple"]
for i in fruits:
    print(i)

fruits[2] = "burger"
for i in fruits:
    print(i)

fruits.append("kiwi")
print(fruits[3])
fruits.remove("burger")
fruits.insert(2, "blueberry")
print("\n")
for i in fruits:
    print(i)

#append will add a element, remove will remove it. and insert() will insert a value at a given index.
#The sort() method will sort everything in the list by alphabetical order.
print("\n")
fruits.sort()
print(fruits)


#To reverse use the reverse method.
fruits.reverse() #If want to reverse in alphabetical order use sort() first.
#clear() method will remove everything from the list.

#.index() method will return the position of any object called upon, if not in the list you will receive a error.

print(fruits.index("blueberry"))

#the .count() method will count how many times something is in a list.

fruits.clear()
print(type(fruits))

fruits = {"apple", "orange", "banana", "coconut"} #This is a set, you can not alter the values, but u can add and remove elements. No duplicates.

print(fruits)
print(len(fruits))
#You cannnot use indexing on a set because they are unordered.

fruits.add("pineapple")
print(fruits)
fruits.remove("apple")
print(fruits)

#You can use the pop() method but it will remove something random since sets are unordered.

fruits.clear()
print(type(fruits))

#Tuples are ordered and unchangeable, duplicates are okay and they are faster than lists.
food = ("rice", "burgers", "cheese", "milk")
print(type(food))
print("milk" in food)
print(food.index("rice"))

for foo in food:
    print(foo)


