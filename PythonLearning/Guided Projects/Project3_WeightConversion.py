#Really light very easy project, I wont be exception handling like I did in project 2 for the sake of time,
#I also want to speed up my learning, so ill try to keep these projects my beginner level. I dont want to get to technical.
#This project will be an extremely easy kg to lb or lb to kg weight converter.
#Project 3.
weight = float(input("How much do you weight? "))
weighthold = weight
whatunit = str(input("Are you weighing yourself in kilograms or pounds? kg/lbs "))
if whatunit == "kg":
    weight = weight * 2.2
    print(f"Your weight in kilograms, {weighthold}, converted into pounds is {round(weight, 2)}. \n")
else:
    weight = weight / 2.2
    print(f"Your weight in pounds, {weighthold}, converted into kilograms is {round(weight, 2)}. \n")

#Very simple very easy, lightwork took me maybe 3 minutes.
#Also introduced me to the round(?,?) method/function, takes a variable and the decimal place to round to.
#End of Project 3.