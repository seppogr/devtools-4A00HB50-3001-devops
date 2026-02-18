import random
import string

length = 12

nolowercase = False
nouppercase = False
nodigits = False
nosymbols = False

def main(params):
    charset = ""
    if not nolowercase: charset += string.ascii_lowercase
    if not nouppercase: charset += string.ascii_uppercase
    if not nodigits:    charset += string.digits
    if not nosymbols:   charset += string.punctuation

    password = "".join(random.choice(charset) for _ in range(length))
    print(password)
