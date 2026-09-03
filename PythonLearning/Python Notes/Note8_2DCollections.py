#To create a 2D list, you first need a 1D list.

fruits = ["apples", "oranges", "tomatoes"]
vegetables =  ["celery", "broccoli", "cabbage"]
meats = ["ham", "turkey", "steak"]

groceries = [fruits, vegetables, meats] #By adding your 1d list to a new list it becomes a 2d list.
#Each individual list is a row and every item within the list is a column.

print(groceries[0][1])

for i in groceries:
    for k in i:
        print(k, end=" ")
    print()

#This is how 2d list works in python, even 3D list and so on can be created, but it gets much more complicated.


