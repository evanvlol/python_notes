from PasswordStrCheck import PasswordStrength
import time

filepath = "/PythonLearning/Unguided Projects (personal)/passwords.txt"


def score_password(checker):
    score = 0
    score += 1 if checker.len_complexity() else 0
    score += 1 if checker.case_complexity() else 0
    score += 1 if checker.symbol_complexity() else 0
    return score

with open(filepath, "r") as file:
    for line in file:
        words = line.strip()

        check = PasswordStrength()
        check.set_password(words)

        score = score_password(check)

        match score:
            case 0:
                print(f"{words:12} - Extremely weak password.")
            case 1:
                print(f"{words:12} - Weak password.")
            case 2:
                print(f"{words:12} -  Medium strength password.")
            case 3:
                print(f"{words:12}, Strong password.")

        print("=--------------------------------------------------------------------------=")

