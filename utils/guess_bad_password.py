import random

#def main():
name = input("What is your name? ")

print(f'Good Luck {name}!')

badPasswords =[
    "admin", "password", "12345", "iloveyou", "qwerty",
    "abc123", "654321", "p@ssw0rd"
]

badPassword = random.choice(badPasswords)

print("Guess the characters")
print(f'Try to guess a bad password before time runs out.')

guesses = ''
turns = 12

while turns > 0:

    failed = 0

    for char in badPassword:

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The bad password is: ", badPassword)
        break

    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in badPassword:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")
