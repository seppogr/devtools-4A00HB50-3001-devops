# Devtools Git group project

This project is about working together on GitHub, managing version control and upholding to good Git practices.
Tools are called from with ´python devtools.py <scriptName> <params> <params> ...´

## Devtools we developed:

### Password generator

The password generator can take multiple promps and generate strong passwords.
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Command:
--passwordgenerator | -pg           –   Generating password with default setting

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Options:
--nolower   | -nl                   –      Exclude lowercase characters
--noupper   | -nu                   –      Exclude uppercase characters
--nodigits  | -nd                   –      Exclude digits
--nosymbols | -ns                   –      Exclude symbols
--length=<value> | -l=<value>       –      Add custom length for the password
--multiple=<value> | -m=<value>     –      Customize amount of passwords made
--save      | -same                 –      Save passwords to a default file
--save=<path> | -s=<path>           –      Save passwords to custom path
--verbose   | -v                    –      Show each options state
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Combining options example:
-pg -nl -nd -ns
Custom length setting example:
-pg --length=25
Multiple password generation example:
-pg --multiple=5
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Help:
--Help                              –     Display utils/docs/pg_help.txt

––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

