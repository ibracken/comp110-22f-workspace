"""ex01: I am creating Chardle, which is similar to Wordle"""

__author__ = "730563276"

"""Variables"""
full_word = input("Enter a 5-character word:")
if len(full_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single_letter = input("Enter a single character:")
if len(single_letter) != 1:
    print("Error: Character must be a single character.")
    exit()
letter1 = full_word[0]
letter2 = full_word[1]
letter3 = full_word[2]
letter4 = full_word[3]
letter5 = full_word[4]
counter = 0


"""Counter tracker"""
if single_letter == letter1:
    counter = int(counter+1)

if single_letter == letter2:
    counter = int(counter+1)

if single_letter == letter3:
    counter = int(counter+1)

if single_letter == letter4:
    counter = int(counter+1)

if single_letter == letter5:
    counter = int(counter+1)

"""Printing functions"""
print ("searching for " + (single_letter) + (" in ") + (full_word))


if single_letter == letter1:
    print(single_letter + " found at index 0")

if single_letter == letter2:
    print(single_letter + " found at index 1")

if single_letter == letter3:
    print(single_letter + " found at index 2")

if single_letter == letter4:
    print(single_letter + " found at index 3")

if single_letter == letter5:
    print(single_letter + " found at index 4")

if counter > 1:
    print(str(counter) +  " instances of " + single_letter + " found in " + full_word )

if counter == 1:
        print(str(counter) +  " instance of " + single_letter + " found in " + full_word )
else:
        print("no instances of " + single_letter + " found in " + full_word)