class Wrestler:
    no_of_matches = 15

    # Constructor
    def __init__(self, name, belt):
        self.name = name
        self.belt = belt


    def print_detail(self):
        return f"{self.name} is the {self.belt}."

    @classmethod
    def change_matches(cls, update_no_of_matches):
        cls.no_of_matches = update_no_of_matches

    @classmethod
    def alternative_constructor(cls, string):
        # param = string.split("-")
        # return cls(param[0], param[1])
        return cls(*string.split("-"))

    # Without self function
    @staticmethod
    def print_good(string):
        return f"This is Good {string}."

    def __add__(self, other):
        return self.name + other.belt

roman = Wrestler("Roman Reign", "WWE universal Champion")
dean = Wrestler("Dean Ambrose", "Inter Continental Champion")
john = Wrestler.alternative_constructor("John Cena-United state Champion")

# roman.name = "Roman Reign"
# roman.belt = "WWE Universal Champion"

# print(roman.print_detail(), dean.print_detail())
# roman.no_of_matches = 10
# print(roman.no_of_matches)
# print(Wrestler.no_of_matches)
# print(roman.__dict__)
# Wrestler.no_of_matches = 20
# print(Wrestler.no_of_matches)
# print(roman.no_of_matches)
# print(Wrestler.__dict__)

# Wrestler.change_matches(90)
# print(Wrestler.no_of_matches)

# roman.change_matches(32)
# print(roman.no_of_matches)

print(john.print_detail())

print(john.print_good("thing"))
print(john + roman)

