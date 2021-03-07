RIGHT_PASSWORD = 2946


def validate():
    user_guess = input("Insert your password: ")
    if user_guess == str(2946):
        print("Right password!")

    else:
        print("Wrong password, try again!")
        validate()


validate()
