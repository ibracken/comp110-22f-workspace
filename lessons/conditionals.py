"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I am thinking of a number between 1-5,, what is it?")
guess: int = int(input("What is your guess"))

if guess == SECRET:
    print("You are right!!!")
else:
    print("Sorry that is wrong")
    if guess > SECRET:
        print("You guessed too high")
    else:
        print("You gussed too low")

print("Game over.")