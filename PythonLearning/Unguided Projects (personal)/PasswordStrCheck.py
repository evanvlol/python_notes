import string
class PasswordStrength:
    def __init__(self):
        self.password = ""

    def set_password(self, userpswd):
        self.password = userpswd

    def case_complexity(self):
        upper = any(s.isupper() for s in self.password)
        lower = any(s.islower() for s in self.password)
        digit = any(s.isdigit() for s in self.password)

        if not digit:
            print("Your password does not contain any digits.")
        if not upper and not lower:
            print("Your password does not contain upper-case and lower-case alphabetical characters.")
            return False
        if not digit:
            return False
        return True

    def len_complexity(self):
        complexity = True if len(self.password) >= 12 else False
        if not complexity:
            print("Your password does not meet the minimum length requirement of 12 characters.")
            return False
        return True

    def symbol_complexity(self):
        complexity = any(s in string.punctuation for s in self.password)
        if not complexity:
            print("Your password does meet the requirement of at least one symbol.")
            return False
        return True

def main():
    score = 0
    test = PasswordStrength()
    userpass = input("What is your password? ")
    test.set_password(userpass)

    score = score + 1 if test.len_complexity() is True else score
    score = score + 1 if test.case_complexity() is True else score
    score = score + 1 if test.symbol_complexity() is True else score
    print("-------------------------------------------------------------------------------------------")

    match score:
        case 0:
            print("Extremely weak password.")
        case 1:
            print("Weak password.")
        case 2:
            print("Medium strength password.")
        case 3:
            print("Strong password.")

    if score == 3:
        print("Your password meets all complexity requirements.")

if __name__ == "__main__":
    main()
