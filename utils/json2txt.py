#Imports
import json
import sys

# Usage:
# python devtools.py -js utils/<filename>

# Main function
def main(params):
    print("This is JSON converter")

    # If function does not get proper imputs, guide user and exit.
    if len(params) < 3:
        print("Usage: python devtools.py -js <filename>")
        sys.exit(1)

    # Choose the file on CLI.
    filename = params[2]

    # Convert JSON to Python data object.
    with open(filename, "r") as f:
        data = json.load(f)

    # Iterate over each entry and print results based on file name
        for entry in data:
            if "jsonfile.json" in filename:
                # Original people JSON
                print(entry["id"], entry["name"], entry["age"])
            elif "jsonfile2.json" in filename:
                # Pizza JSON
                print(entry["id"], entry["name"], entry["size"], entry["toppings"])
            else: # Fallback for unexpected files
                print("Wrong filename")