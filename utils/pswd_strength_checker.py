import re

def main():
    password_max_points = 3
    password_score = 0
    password = input("Enter password to be checked: ").lower()
    badPasswords = {
        "admin", "password", "12345", "iloveyou", "qwerty",
        "abc123", "654321", "p@ssw0rd"
        }

    print(f'Analysis for your password:')
    # This will check for password length

    if len(password) < 6:
        print(f'Password is too short (less than 6 characters).')
    else:
        print(f'Password length is six or more characters.')
        password_score += 1

    # # this will check if the password contains numbers or special characters
    # if (bool(re.search(r"(\d|[^A-Za-z0-9\s])", password))):
    #     print(f'Password contains special characters or numbers.')
    #     password_score += 1
    # else:
    #     print(f'No special characters or numbers found.')

    def has_lower(password):
        return re.search(r"[a-z]", password)

    if has_lower(password):
        password_score += 1

    def has_upper(password):
        return re.search(r"[A-Z]", password)

    if has_upper(password):
        password_score += 1


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

# print if there are 3 or more
    if check_for_long_repeat(password) != None:
        print(f'The password contains {check_for_long_repeat(password)} repeating characters in row. Only two allowed.')
    else:
        print(f'The password does not contain more than two same characters in row.')
        password_score += 1


# Give final score to user
    print(f'Your password score is {password_score}/{password_max_points}')

