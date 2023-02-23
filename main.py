from random import randint


INPUT_MESSAGE = "Enter your guess!"
INPUT_AGAIN_MESSAGE = "Try to enter your guess again!"


def main():
    input_message = INPUT_MESSAGE
    print("Welcome to the NumberGuesser!")
    while True:
        guess = input(input_message)
        if is_valid(guess):
            guess = int(guess)
            input_message = INPUT_MESSAGE
        else:
            print("You probably entered wrong number.")
            input_message = INPUT_AGAIN_MESSAGE
            continue


def is_valid(user_input: object) -> bool:  # Checking for valid input value
    try:
        user_input = int(user_input)
    except ValueError:
        return False
    if 1 <= user_input <= 100:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_valid(input()))
