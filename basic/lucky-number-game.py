import random

def lucky_number_game():
    lucky_number = random.randint(1, 100)

    while True:
        user_number = int(input("Guess your lucky number: "))

        if user_number == lucky_number:
            print("Congratulations! You won the game.")
            break
        elif user_number >= lucky_number:
            print("You entered higher than lucky number.\n")
        elif user_number <= lucky_number:
            print("You entered lower than lucky number.\n")

lucky_number_game()