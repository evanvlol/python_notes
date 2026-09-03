#An iterable is a category. Any object or collection that can return its elements one at a time is considered iterable.

numbers = [1,2,3,4,5]

def main():
    for i in numbers:
        if i is not len(numbers):
            print(f"{i}", end = ", ")
        else: print(f"{i}.")


main()

#Peep that the list is iterable because we can return element in it once at a time.
