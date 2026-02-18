import sys
import utils.password_generator as pg
import utils.json2txt as js
import utils.pswd_strength_checker as psc

def switch(params):
    if len(params) > 1:
        if params[1] == "--hello":
            print("Hello World!")
        elif params[1] == "--passwordgenerator" or params[1] == "-pg":
            pg.main(params)
        elif params[1] == "--jsonconverter" or params[1] == "-js":
            js.main()
        elif params[1] == "--pswdchk":
            psc.main()
        else:
            print("Please input a valid command.")
    else:
        print("No command inserted.")


# Parameter array.
params = sys.argv
switch(params)
