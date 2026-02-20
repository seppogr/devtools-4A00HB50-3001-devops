import re

def main():
    password = input("Enter password to be checked: ").lower()
    badPasswords = {
        "admin", "password", "12345", "iloveyou", "qwerty",
        "abc123", "654321", "p@ssw0rd"
        }

    print(f'Analysis for your password:')
    # This will check for password length

    if len(password) < 6:
        print(f'Password is really short (less than 6 characters).')
    else:
        print(f'Looks ok length.')

    # this will check if the password contains numbers or special characters
    if (bool(re.search(r"(\d|[^A-Za-z0-9\s])", password))):
        print(f'Password contains special characters or numbers.')
    else:
        print(f'No special characters or numbers found.')

