import random
import string

length = 12

nolowercase = False
nouppercase = False
nodigits = False
nosymbols = False

def checkParams(param):
    global nolowercase, nouppercase, nodigits, nosymbols

    if param == "--nolower" or param == "-nl":
        nolowercase = True
    elif param == "--noupper" or param == "-nu":
        nouppercase = True
    elif param == "--nodigits" or param == "-nd":
        nodigits = True
    elif param == "--nosymbols" or param == "-ns":
        nosymbols = True

def main(params):
    for param in params:
        checkParams(param)

    charset = ""
    if not nolowercase: charset += string.ascii_lowercase
    if not nouppercase: charset += string.ascii_uppercase
    if not nodigits:    charset += string.digits
    if not nosymbols:   charset += string.punctuation

    password = "".join(random.choice(charset) for _ in range(length))
    print(password)
