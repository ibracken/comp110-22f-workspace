"""In both games, the player fights a dragon. One mode is more difficult than the other."""


__author__ = 730563276

from random import randint


player: str = ""
points: int = 0


NAMED_CONSTANT = "\U00000000"
EMOJI_HAPPY = "\U0001F600"
DEATH_EMOJI = "\U0001F635"


def greet() -> None:
    """Welcomes the player to the game."""
# takes the global player variable
    global player
# Greets the player
    player = input("What is your name? ")
    print(f"Welcome to the game {player}! {EMOJI_HAPPY}")


def easy():
    """Easy mode where the dragon does less damage and you do more damage."""
    # Importing global variables
    global player
    global points
    # Setting the health and damage variables for you and the dragon
    dragon_health = 1000
    your_health = 1000
    your_damage = 0
    dragon_damage = 0
    # Intro to the game
    print(f"Hi {player}, welcome to easy mode. In this game you will be fighting a dragon. If you win without dying you will get 10 points but if you lose you get nothing.")
    print("You have two possible options for fighting, you can either use your 'safe' attack or your 'risky' attack.")
    print("Your safe attack will do a similar amount of damage each time while your risky attack will vary wildly.")
    # Actual game loop
    while dragon_health > 0 and your_health > 0:
        move = input(f"Your health is at {your_health} and the dragon's health is at {dragon_health}, what attack will you use? ")
    # If the user selects the safe move option
        if move == "safe":
            your_damage = randint(80, 120)
            dragon_damage = randint(70, 90)
            print(f"You did {your_damage} to the dragon but it did {dragon_damage} to you!")
            dragon_health = (dragon_health - your_damage)
            your_health = (your_health - dragon_damage)
    # If the user selects the risky move option
        elif move == "risky":
            your_damage = randint(1, 220)
            dragon_damage = randint(70, 90)
            print(f"You did {your_damage} to the dragon but it did {dragon_damage} to you!")
            dragon_health = (dragon_health - your_damage)
            your_health = (your_health - dragon_damage)
    # If the user responds with anything else
        else:
            print("please respond with either 'safe' or 'risky'.")
    if your_health < 0:
        print(f"Im sorry, you died, your points remain at {points}. {DEATH_EMOJI}")
    else:
        points += 10
        print(f"Congrats, You beat the dragon! Your total points have increased to {points}! {EMOJI_HAPPY}")


def hard(num: int) -> int:
    """Hard mode where the dragon does more damage and you do less damage."""
    # Importing global variable
    global player
    # Setting the health and damage variables for you and the dragon
    dragon_health = 1000
    your_health = 1000
    your_damage = 0
    dragon_damage = 0
    # Intro to the game
    print(f"Hi {player}, welcome to hard mode. In this game you will be fighting a dragon. If you win without dying you will get 50 points but if you lose you get nothing.")
    print("You have two possible options for fighting, you can either use your 'safe' attack or your 'risky' attack.")
    print("Your safe attack will do a similar amount of damage each time while your risky attack will vary more.")
    # Actual game loop
    while dragon_health > 0 and your_health > 0:
        move = input(f"Your health is at {your_health} and the dragon's health is at {dragon_health}, what attack will you use? ")
    # If the user selects the safe move option
        if move == "safe":
            your_damage = randint(70, 120)
            dragon_damage = randint(70, 130)
            print(f"You did {your_damage} to the dragon but it did {dragon_damage} to you!")
            dragon_health = (dragon_health - your_damage)
            your_health = (your_health - dragon_damage)
    # If the user selects the risky move option
        elif move == "risky":
            your_damage = randint(1, 200)
            dragon_damage = randint(70, 130)
            print(f"You did {your_damage} to the dragon but it did {dragon_damage} to you!")
            dragon_health = (dragon_health - your_damage)
            your_health = (your_health - dragon_damage)
    # If the user responds with anything else
        else:
            print("please respond with either 'safe' or 'risky.'")
    # If user dies
    if your_health < 0:
        print(f"Im sorry, you died. Your points remain at {num}. {DEATH_EMOJI}")
        return num
    # If user wins
    else:
        num += 50
        print(f"Congrats, You beat the dragon! Your total points have increased to {num}! {EMOJI_HAPPY}")
        return num


def main() -> None:
    """Main function that ties all the other together to form the full game."""
    # Defining variables
    global points
    loop = True
    choice = ""
    # greet function
    greet()
    # game loop
    while loop is True:
        print("There are a couple options to choose from.")
        print("You can either play the easy mode by typing 'easy' or the hard mode by typing 'hard'.")
        choice = input("You can also choose to exit the game by typing 'quit'. ")
        if choice == "easy":
            easy()
        elif choice == "hard":
            points = hard(points)
        elif choice == "quit":
            loop = False
        else:
            print("Please respond with either 'easy', 'hard', or 'quit'.")
  

if __name__ == "__main__":
    main()