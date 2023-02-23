from random import randint


def main():
    print("Welcome to the NumberGuesser!")
    while True:
        guess = input("Enter your guess!")
        if is_valid(guess):
            guess = int(guess)
        else:
            print("You probably entered wrong number.")


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
