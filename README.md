# Devtools Git group project

This project is about working together on GitHub, managing version control and upholding to good Git practices.
Tools are called with:
`python devtools.py <scriptName> <params> <params>`

## Devtools we developed:

### Password generator

The password generator can take multiple promps and generate strong passwords.
---
Command:
--passwordgenerator | -pg           –   Generating password with default setting

---
Options:
| Option | Description |
|--------|-------------|
| `--nolower` / `-nl` | Exclude lowercase characters |
| `--noupper` / `-nu` | Exclude uppercase characters |
| `--nodigits` / `-nd` | Exclude digits |
| `--nosymbols` / `-ns` | Exclude symbols |
| `--length=<value>` / `-l=<value>` | Set custom password length |
| `--multiple=<value>` / `-m=<value>` | Generate multiple passwords |
| `--save` / `-same` | Save passwords to default file |
| `--save=<path>` / `-s=<path>` | Save passwords to custom path |
| `--verbose` / `-v` | Show each option state |
---
Combining options example:
| Example | Command |
|---------|---------|
| Combining options | `-pg -nl -nd -ns` |
| Custom length | `-pg --length=25` |
| Multiple passwords | `-pg --multiple=5` |
---
Help:
--Help                              –     Display utils/docs/pg_help.txt

---
### Password strenght checker

This utility will ask for a password in a prompt and check if it passes the following tests:
It will rate the strenght of your password on a scale of 0-7.
---
Command:
--pswdchk                   - Asks for a password and analyses its strength

---
- not in the most common list
- has numbers
- has symbols
- has uppercase
- has lowercase
- is longer than 6 characters
- has no more than 2 same characters in row, eg "aa" is allowed but "aaa" is not

---
### Guess bad password hangman game

A fun way to learn what passwords not to use. A hangman game of bad choices!!!
---
Command:
--guessbadpassword or -gbp

---
### JSONconverter

Convert JSON data from utils/<filename> to Python data object and display it in terminal.
It will adjust dynamically to the amount of keys in the JSON object.
---

This is JSON converter
id: 1, name: Margherita, size: Medium, toppings: ['Cheese', 'Tomato']
id: 2, name: Pepperoni, size: Large, toppings: ['Cheese', 'Tomato', 'Pepperoni']
id: 3, name: Hawaiian, size: Medium, toppings: ['Cheese', 'Tomato', 'Ham', 'Pineapple']

This is JSON converter
id: 1, name: bob, age: 22
id: 2, name: alice, age: 21
id: 3, name: tony, age: 22

Command:
--jsonconverter utils/<filename> or -js utils/<filename>
---
