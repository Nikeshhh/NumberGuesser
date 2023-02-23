from random import randint


def main():
    print("Welcome to the NumberGuesser!")


def is_valid(user_input: object) -> bool:  # Checking for valid input value
    if isinstance(user_input, int):
        if 1 <= user_input <= 100:
            return True
    else:
        return False


if __name__ == '__main__':
    main()
