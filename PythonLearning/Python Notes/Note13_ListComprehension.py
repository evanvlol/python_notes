#List comprehension is a easier way to create list in python.
#They are more compact and easier to read than traditional loops.

#ex using traditional loop.

def main():
    numbers = []
    for x in range(1,11):
        numbers.append(x * 2)
    print(numbers)
    numbers = [x * 3 for x in range(1, 11)] #Basically, what you want to do comes first, then your loop.
    print(numbers)

    #Below im going to try something a little more complicated using an if statement to multiply numbers only if they ar even.
    numbers = [x * 5 if x % 2 == 0 else x for x in range(1, 11)] # Take x and multiply it by 5 if the number is even, else just include it as it is in the list.
    print(numbers)
    

main()

