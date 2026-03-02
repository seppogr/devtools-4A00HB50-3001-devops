#Imports
import json
import sys

# Main function
def main():
    print("This is JSON converter")

    # If function does not get proper imputs, guide user and exit.
    if len(sys.argv) != 2:
        print("Usage: python json2txt.py <filename>")
        sys.exit(1)


    filename = sys.argv[1]

    with open(filename, "r") as f:
        data = json.load(f)

    for entry in data:
        print(entry["id"], entry["name"], entry["age"])

if __name__ == "__main__":
    main()