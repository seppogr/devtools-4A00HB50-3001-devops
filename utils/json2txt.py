#Imports
import json
import sys

# Usage:
# python json2txt.py <filename> (jsonfile.json)

# Main function
def main():
    print("This is JSON converter")

    # If function does not get proper imputs, guide user and exit.
    if len(sys.argv) != 2:
        print("Usage: python json2txt.py <filename>")
        sys.exit(1)

    # Choose the file on CLI.
    filename = sys.argv[1]

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

# This line ensures that main() runs only when the script is executed directly
if __name__ == "__main__":
    main()