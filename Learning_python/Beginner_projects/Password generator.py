import random

PASSWORD_LENGTH = 9
LETTERS = "qwertyuiopüõasdfghjklöäzxcvbnm"
CAPITAL_LETTERS = "QWERTYUIOPÜÕASDFGHJKLÖÄZXCVBNM"


def generate():
    number_or_letter = 0
    capital_or_not = 0
    password = []
    for value in range(PASSWORD_LENGTH):
        number_or_letter = random.randint(1, 2)
        if number_or_letter == 1:
            password.append(random.randint(0, 9))

        elif number_or_letter == 2:
            capital_or_not = random.randint(1, 2)
            if capital_or_not == 1:
                password.append(random.choice(CAPITAL_LETTERS))

            if capital_or_not == 2:
                password.append(random.choice(LETTERS))

    print(str(password))


generate()
