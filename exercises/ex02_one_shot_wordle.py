"""ex01: I am creating Wordle, the popular game where you guess a word in 6 tries"""

__author__ = "730563276"

"""variables and emojis"""
secret_word = str("python")
user_guess = input("What is your " + str(len(secret_word)) + " letter guess? ")
index_variable = int(0)
emoji = ""
guessed_character = bool(False)
alt_index = int(0)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


"""setting up the guesses"""
while len(user_guess) != len(secret_word):
    user_guess = input("That was not " + str(len(secret_word)) + " letters! Try again: ")


"""Checking to see if letter equals word"""
while index_variable < len(secret_word):
    guessed_character = False
    if user_guess[index_variable] == secret_word[index_variable]:
        emoji += GREEN_BOX
        index_variable += 1
    else:
        while guessed_character == False and alt_index < len(secret_word):
            if user_guess[index_variable] == secret_word[alt_index]:
                guessed_character = True
            else:
                alt_index += 1
        if guessed_character == True:
            emoji += YELLOW_BOX
            index_variable += 1
            alt_index = 0
        else:
            emoji += WHITE_BOX
            index_variable += 1
            alt_index = 0


print(emoji)



"""Checking if correct"""
if user_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
