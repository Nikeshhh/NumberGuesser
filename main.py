from random import randint


INPUT_MESSAGE = "Enter your guess!\n"  # Standard input message
INPUT_AGAIN_MESSAGE = "Try to enter your guess again!\n"  # Input message after invalid input
INPUT_TRY_AGAIN = "Try to guess again!\n"


def main():  # Main program function
    print("Welcome to the NumberGuesser!")

    while True:
        user_guess = input_number(input(INPUT_MESSAGE))
        right_guess = randint(1, 100)

        guess_flag = check_guess(user_guess, right_guess)
        while guess_flag is False:
            user_guess = input_number(input(INPUT_TRY_AGAIN))
            guess_flag = check_guess(user_guess, right_guess)


def check_guess(user_guess: int, right_guess: int) -> bool:  # Main game function
    if right_guess < user_guess:
        print("The right number is below your guess!")
        return False
    elif right_guess > user_guess:
        print("The right number is above your guess!")
        return False
    else:
        print("This is the number, congratulations!")
        return True


def input_number(number: str) -> int:  # Checks number, entered by user and returns it as int when it is valid
    while is_valid(number) is False:
        number = input(INPUT_AGAIN_MESSAGE)
    return int(number)


def is_valid(user_input: object) -> int or bool:  # Checking for valid input value
    try:
        user_input = int(user_input)
    except ValueError:
        print("You probably entered not a number.")
        return False
    if 1 <= user_input <= 100:
        return user_input
    else:
        print("You probably entered wrong number.")
        return False


if __name__ == '__main__':
    main()
