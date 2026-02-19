
def main():
    password = input("Enter password to be checked: ").lower()
    badPasswords = {
        "admin", "password", "12345", "iloveyou", "qwerty",
        "abc123", "654321", "p@ssw0rd"
    }

#check if password is in the common list
    if password in badPasswords:
        print(f'Password is very common!')

    if len(password) < 6:
        print(f'Password is really short')
    else:
        print(g'Looks ok length)


# pswd_strength_checker
