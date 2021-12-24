import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a Number between 1 and {x}: "))
        print(guess)
        if guess < random_number:
            print("Sorry, guess again! Too low")
        elif guess > random_number:
            print("Sorry, guess again! Too high")

    print(f"Congrats! You have guessed correctly {random_number}")

guess(10)


def computer_guess(x):
    print("Think of a number between 1 and 10")
    global Guess
    low = 1
    high = x
    feedback = ' '
    while feedback != 'c':
        if low != high:
            Guess = random.randint(low, high)
        else:
            Guess = low
        feedback = input(f"Is {Guess} too high (H), too Low (L), or Correct (C)?").lower()
        if feedback == 'h':
            high = Guess - 1
        elif feedback == 'l':
            low = Guess + 1
    print(f"The computer guess your number, {Guess}, correctly")


computer_guess(10)