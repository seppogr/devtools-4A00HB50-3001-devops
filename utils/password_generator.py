import random
import string
import os
from datetime import datetime
from utils.printFile import printFile

passwordsArr = []

length = 12
amountToGenerate = 1
subdir = "./utils/docs"

nolowercase = False
nouppercase = False
nodigits = False
nosymbols = False
savepwds = False
verbose = False

def save_passwords(passwords, subdir, filename="passwords.txt"):
    os.makedirs(subdir, exist_ok=True)
    filepath = os.path.join(subdir, filename)

    with open(filepath, 'a') as f:
        f.write(f"\n# {datetime.now()}\n")
        for pwd in passwords:
            f.write(pwd + "\n")
    print(f"Passwords saved to {filepath}")

def checkParams(param):
    global length, amountToGenerate, subdir, nolowercase, nouppercase, nodigits, nosymbols, savepwds, verbose

    if param == "--help" or param == "-h":
        printFile("utils/docs/pg_help.txt")
        exit(1)
    elif param == "--nolower" or param == "-nl":
        nolowercase = True
    elif param == "--noupper" or param == "-nu":
        nouppercase = True
    elif param == "--nodigits" or param == "-nd":
        nodigits = True
    elif param == "--nosymbols" or param == "-ns":
        nosymbols = True
    elif param == "--verbose" or param == "-v":
        verbose = True
    elif param == "--save" or param == "-s":
        savepwds = True

    elif param.startswith("--save=") or param.startswith("-s="):
        try:
            savepwds = True
            subdir = param.split("=")[1]
        except IndexError:
            print("Error: --save requires a directory path after '=' (example: --save=./mydir)")
            exit(1)

    elif param.startswith("--multiple=") or param.startswith("-m="):
        try:
            amountToGenerate = int(param.split("=")[1])
        except ValueError:
            print("Invalid value for multiple passwords.")
            exit()


    elif param.startswith("--length=") or param.startswith("-l="):
        try:
            length = int(param.split("=")[1])
        except ValueError:
            print("Invalid length value.")
            exit()

    elif param == "-pg" or param == "--passwordgenerator" or param == "devtools.py":
        return

    else:
        print("Invalid extension. For all accessible extensions check: '-pg -h' or --passwordgenerator --help")
        exit(1)

def main(params):
    global amountToGenerate

    for param in params:
        checkParams(param)

    charset = ""
    if not nolowercase: charset += string.ascii_lowercase
    if not nouppercase: charset += string.ascii_uppercase
    if not nodigits:    charset += string.digits
    if not nosymbols:   charset += string.punctuation

    if not charset:
        print("Error: all character sets excluded.")
        return

    if verbose:
        print("Options:\n")
        print(f"nolowercase = {nolowercase}")
        print(f"nouppercase = {nouppercase}")
        print(f"nodigits = {nodigits}")
        print(f"nosymbols = {nosymbols}")
        print(f"save = {savepwds}")
        print(f"amount to generate = {amountToGenerate}")
        print(f"pwd length = {length}")
        print("\nPasswords:\n")

    while amountToGenerate > 0:
        password = "".join(random.choice(charset) for _ in range(length))
        print(password)
        passwordsArr.append(password)
        amountToGenerate -= 1

    if (savepwds):
            save_passwords(passwordsArr, subdir)
