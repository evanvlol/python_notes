def dayofweek(day):
    match day:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")

def animalcase(char):
    match char:
        case "a":
            print("Ant-eater")
        case "b":
            print("Bear")
        case "c":
            print("Cat")

def main():
    day = str(input("Enter a number 1-7 or a letter 'a-c' to find out what day of the week it is. "))
    if day.isdigit():
        day = int(day)
    animalcase(day)
    dayofweek(day)

main()
