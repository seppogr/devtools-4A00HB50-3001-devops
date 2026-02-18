
def main():
    password = input("Enter password to be checked: ")
    badPasswords = {
        "admin", "password", "12345", "iloveyou", "qwerty",
        "abc123", "654321", "p@ssw0rd"
    }

    if password in badPasswords:
        print("Password is very common")
