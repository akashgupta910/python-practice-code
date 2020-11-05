# PROPERTY, SETTERS AND PROPERTY DECORATORS

# AND ALSO TALK ABOUT OBJECT INTROSPECTION

class User:

    def __init__(self ,fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def print_username(self):
        return f"Name of Username is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Invalid Email address"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):

        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


roman_reign = User("Roman","Reign")

roman_reign.fname = "Seth"
roman_reign.lname = "Rollins"
roman_reign.fname = "Dolph"

print(roman_reign.email)

roman_reign.email = "roman.reign@gmail.com"

print(roman_reign.email)

del roman_reign.email

print(roman_reign.email)

# LET'S START OBJECT INTROSPECTION

print(type(roman_reign))
print(id(roman_reign))
print(dir(roman_reign))

import inspect

print(inspect.getmembers(roman_reign))




