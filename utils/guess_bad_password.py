import random

#def main():
name = input("What is your name? ")

print(f'Good Luck {name}! Try to guess a bad password before time runs out.')

badPasswords =[
    "admin", "password", "12345", "iloveyou", "qwerty",
    "abc123", "654321", "p@ssw0rd"
]

word = random.choice(badPasswords)

print("Guess the characters")
print(f'{word}')

guesses = ''
turns = 12