import os
import random

correctWord = ""

guess = ""

drawLine = []

guess_counter = 0
guess_wrong_counter = 0
gameOver = False

correctWord = input("What is the word you want the player to guess? ")
os.system("cls")

for i in range(len(correctWord)):  # Loop X amount of time depending on how many characters are in the correct word string

    drawLine += "_"  # Saves the amount of blank spaces needed for each character depending on the length of the correct word

while guess != correctWord and not gameOver:  # Using not in to check for boolean...?

    # print(drawLine)  # Prints the blank spaces

    """
    for i in drawLine:   # A crude way to check if the game if over if the player only receives the hints to get a victory
        count = 0
        if i == "_":
            count = count + 1
        else:
            count = 0
            if count == 0:
                gameOver = True
    """
    os.system("cls")

    print(" ".join(drawLine))  # Have no idea how it works, but it removes the quotes when printing out list

    print("Guesses made: " + str(guess_counter))
    guess = input("Guess the word: ")
    # guess = guess[0].upper() + guess[1:]  # Converts the first character of guess into uppercase and appends the rest of the word in the string to build a new one
    print("Guess " + guess + " is wrong." + "\n\n")
    guess_wrong_counter += 1
    guess_counter += 1

    if guess_wrong_counter == 4:  # Give a random character hint to the player after 4 incorrect attempts
        print("")

        randomValue = int(random.randint(0, len(correctWord) - 1))  # Picks a random number from 0 to the max length of the correct word. -1 to prevent from going out of bounds

        #  print(randomValue) Debug purposes

        drawLine[randomValue] = correctWord[randomValue]  # Assigns a random character from the correct word to the blank line

        guess_wrong_counter = 0

print("\n\n")
print("The word is " + correctWord)
print("It took you " + str(guess_counter) + " guesses!")

exit_input = ""
exit_input = input("Press Enter to exit...")