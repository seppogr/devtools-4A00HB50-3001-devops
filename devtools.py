import sys
import utils.password_generator as pg

def switch(params):
    if len(params) > 1:
        if params[1] == "--hello":
            print("Hello World!")
        elif params[1] == "--passwordgenerator" or "-pg":
            pg.main()
        else:
            print("Please input a valid command.")
    else:
        print("No command inserted.")


# Parameter array.
params = sys.argv
switch(params)
