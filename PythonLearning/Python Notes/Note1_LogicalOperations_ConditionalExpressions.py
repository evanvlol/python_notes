#Note1 is about Logical Operations and Conditional Expressions.

#Logical operators involve conditions such as "or", "and", or "not":

#the or condition will check to see if at least one condition is met, example below.

number = 6
if number == 5 or 6: #Note that it skips 5 because number isn't 5, but still executes and prints "yes" because the number is 6.
    print("Yes")


#the and condition will check to see if both conditions are met, example below
hungry = True
time = "Lunch"
if time == "Lunch" and hungry == True:  #Because both conditions are met, there is no problem in the logic, and it will run fine.
    print("It is lunch time and I am hungry.")

#the not operation will check to see if the opposite condition is not available. see example again using the hungry variable below.
if not hungry:
    print("I am not hungry.") #Notice how this doesn't run, this is because its asking if hungry is NOT true. But hungry is...

#Instead we need to write over hungry to check to see if It's NOT false.
#I'm going to make a new variable called nothungry so it makes more sense.
nothungry = False
if not nothungry:
    print("I am hungry")

#This might sound a little crazy, but if you said "I am not, not hungry, that would be the same as saying you are hungry".

#This is the end of logical operators section.


#Conditional Expressions:
#Conditional expressions are like one-line shortcuts for if else statements
#Example below...

number = 5
result = "EVEN" if number % 2 == 0 else "ODD"
print(result)

#Pretty simple, I might come back and add more examples later but for now this it.



