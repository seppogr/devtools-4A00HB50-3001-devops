# This is a simple hangman game in which the user guesses
# the characters of a word from badPasswords array.
# The words are randomized each time.

import random
def main():
    badPasswords =[
        "admin", "password", "12345", "iloveyou", "qwerty",
        "abc123", "654321", "p@ssw0rd"
    ]

    badPassword = random.choice(badPasswords)
    guesses = ''
    turns = 12
    print(f'Try to guess a bad password before time runs out. You have {turns} guesses remaining.')

    while turns > 0:

        failed = 0
        for char in badPassword:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        print()

        if failed == 0:
            print("You got it!")
            print(f'The bad password is: {badPassword}')
            break

        print()
        guess = input("Guess a character: ")

        guesses += guess

        if guess not in badPassword:

            turns -= 1
            print("Wrong guess.")
            print(f'You have {turns} guesses remaining.')

            if turns == 0:
                print(f'You loose! The bad password was "{badPassword}".')
