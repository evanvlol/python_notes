question = ("What is the capital of France?: ",
            "How many continents are on Earth?: ",
            "What planet is nicknamed the 'Gas Giant'?: ",
            "What is the chemical symbol for water? ",
            "What scientific force keeps everything in place on the ground? ")
options = (("A. Paris", "B. Bordeaux", "C. Marseille", "D. Rome"),
           ("A. 3", "B. 5", "C. 6", "D. 7"),
           ("A. Jupiter","B. Saturn","C. Mars","D. Neptune"),
           ("A. HCl","B. CO2","C. H2O","D. Fe"),
           ("A. Gravity","B. Sonar","C. Radio","D. Virus"))
answers = ("A","D","B","C","A")
guesses = []
score = 0
question_num = 0


for i in question:
    print("----------------------")
    print(i)
    for option in options[question_num]:
        print(option)
    guess = (input("What is your answer (A/B/C/D)? ")).upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"The correct answer is {answers[question_num]}.")
    question_num+=1
print("----------------------")
print(f"Your score is {score * 20}%!")
print("---------THANK YOU-------------")

