import re

def main():
    password_max_points = 7
    password_score = 0
    password = input("Enter password to be checked: ")
    badPasswords = {
        "admin", "password", "12345", "iloveyou", "qwerty",
        "abc123", "654321", "p@ssw0rd"
        }

    print(f'Analysis for your password:')

# Check against the most common passwords
    if password in badPasswords:
        print(f'Password is very common.')
    else:
        print(f'Password is not one of the most common passowrds')
        password_score += 1

# This will check for password length
    if len(password) < 6:
        print(f'Password is too short (less than 6 characters).')
    else:
        print(f'Password length is six or more characters.')
        password_score += 1

# Check for lowercase characters
    def has_lower(password):
        return re.search(r"[a-z]", password)

    if has_lower(password):
        print(f'Password has lower characters.')
        password_score += 1
    else:
        print(f'Password has no lower characters.')

# Check for uppercase characters
    def has_upper(password):
        return re.search(r"[A-Z]", password)

    if has_upper(password):
        print(f'Password has upper characters.')
        password_score += 1
    else:
        print(f'Password has no upper characters.')

# Check for numbers
    def has_digit(password):
        return re.search(r"[0-9]", password)

    if has_digit(password):
        print(f'Password has numbers.')
        password_score += 1
    else:
         print(f'Password has no numbers.')

# Check for special characters
    def has_symbol(password):
        return re.search(r"[^a-zA-Z0-9]", password)

    if has_symbol(password):
        print(f'Password has symbols.')
        password_score += 1
    else:
        print(f'Password has no symbols.')


# Check if the password has 3 or more repeatung chars in a row
    def check_for_long_repeat(password):
        max_repeat = 3
        count = 1
        for i in range(1, len(password)):
            if password[i] == password[i-1]:
                count += 1
                if count >= max_repeat:
                    return count
            else:
                count = 1
        return None

    if check_for_long_repeat(password) != None:
        print(f'The password contains {check_for_long_repeat(password)} repeating characters in row. Only two allowed.')
    else:
        print(f'The password does not contain more than two same characters in row.')
        password_score += 1


# Give final score to user
    print(f'Your password score is {password_score}/{password_max_points}.')

    if password_score < 4:
        print(f'You can try to learn som good passwords by playin our "Guess bad password" -game. Try it today and learn!')

    elif password_score < 2:
        print(f'Maube you could give our password generator a go?')
