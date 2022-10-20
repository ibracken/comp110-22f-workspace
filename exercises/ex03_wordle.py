"""ex01: I am creating Wordle, the popular game where you guess a word in 6 tries."""

__author__ = "730563276"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(letter_series: str, single_character: str) -> bool:
    """single_character will be picked out of letter_series."""
    assert len(single_character) == 1
    i = int(0)
    while i < len(letter_series):
        if letter_series[i] == single_character:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis by using contains_char to test for yellow or white box emojis."""
    assert len(guess) == len(secret)
    i = 0
    emoji = ""
    letter_checker = False
    while i < len(guess):
        letter_checker = False
        if contains_char(secret, guess[i]):
            letter_checker = True
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
            i += 1
        elif letter_checker is True:
            emoji += YELLOW_BOX
            i += 1
        else:
            emoji += WHITE_BOX
            i += 1
    return emoji


def input_guess(length_of_secret: int) -> str:
    """Asks the user for a guess and will continue asking until guess is the correct length."""
    user_guess = input("Enter a " + str(length_of_secret) + " character word: ")
    while len(user_guess) != length_of_secret:
        user_guess = input(("That wasn't " + str(length_of_secret) + " chars! Try again: "))
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_counter = 1
    user_win = False
    user_guess = ""
    secret = "codes"
    emoji = ""
    while turn_counter <= 6 and user_win is False:
        print("=== Turn " + str(turn_counter) + "/6 ===")
        user_guess = (input_guess(len(secret)))
        emoji = emojified(user_guess, secret)
        print(emoji)
        if user_guess == secret:
            print("You won in " + str(turn_counter) + "/6 turns!")
            user_win = True
        else:
            turn_counter += 1
    if user_win is False:
        print("X/6 - Sorry, try again tomorrow!")

        
if __name__ == "__main__":
    main()