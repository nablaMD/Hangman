import random
import string


def hangman_game():

    tries = 8
    list_of_words = ('python', 'java', 'kotlin', 'javascript')
    word_to_guess = random.choice(list_of_words)
    dashes = list(len(word_to_guess) * "-")
    letters = list(string.ascii_lowercase)
    user_letters = []

    while tries > 0:
        print()
        print("".join(dashes))
        user_guess = input("Input a letter: ")
        if len(user_guess) == 1:
            if user_guess in letters:
                if user_guess not in user_letters:
                    user_letters.append(user_guess)
                    if user_guess in word_to_guess:
                        for i in range(len(word_to_guess)):
                            if word_to_guess[i] == user_guess:
                                dashes[i] = user_guess
                        if word_to_guess == "".join(dashes):
                            print("You guessed the word!\nYou survived!")
                            break
                    else:
                        print("That letter doesn't appear in the word")
                        tries -= 1
                else:
                    print("You've already guessed this letter")
            else:
                print("Please enter a lowercase English letter")
        else:
            print("You should input a single letter")
    else:
        print("You lost!")


print("H A N G M A N")

user_will = input("Type \"play\" to play the game, \"exit\" to quit:")

while not user_will == "exit":
    if user_will == "play":
        hangman_game()
    user_will = input("\nType \"play\" to play the game, \"exit\" to quit:")
