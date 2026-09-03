#Another quick project just to get the brain thinking, shouldn't require alot of brain power.
#This project will convert temperature back and forth from Fahrenheit to Celsius and vice versa.
#Project 4.
fORc = str(input("Are you measuring the temperature in Fahrenheit or Celsius degrees (F/C)? "))
tempnumber = int(input("What is the temperature? "))
convertedtemp = None
if fORc == "F":
    convertedtemp = (tempnumber - 32 ) * 5/9
    print(f"{tempnumber} degrees Fahrenheit converted to Celsius is {round(convertedtemp,2)}.")
else:
    convertedtemp = tempnumber * 9/5 + 32
    print(f"{tempnumber} degrees Celsius converted to Fahrenheit is {round(convertedtemp,2)}.")

##Once again another easy project to help understand the fundamentals of if statements in python. Very simple
#and very quick.
#End of Project 4.



