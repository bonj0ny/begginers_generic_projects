import random

"""


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number between 1 and {x} : "))
        if guess < random_number:
            print("Sorry, guess again. Too low")
        elif guess > random_number:
            print("Sorry, guess again. Too high")

    print(f"Congratz, you have guessed the number {random_number}")


guess(20)

"""


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could be also be high b/c low = high
        feedback = input(
            f"Is {guess} too high (H), too low (L) or correct (C)")
        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1

    print(f"Great! the computer guessed your number, {guess},  correctly!")


computer_guess(50)
