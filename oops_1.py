# OOPS PROGRAMMING

class Employee:
    no_of_leaves = 8

harry = Employee()
john = Employee()

harry.name = "Harry"
harry.salary = 6767
harry.role = "Instructor"

john.name = "John Cena"
john.salary = 9089
john.role = "Wrestler"

harry.no_of_leaves = 10
Employee.no_of_leaves = 90
john.no_of_leaves = 87

print(harry.name)
print(harry.__dict__)
print(harry.no_of_leaves)
print(Employee.no_of_leaves)
print(john.no_of_leaves)

# SELF IN OOPS PROGRAMMING

class Ceo:
    def details(self):
        return f"The Name is {self.name}. Salary is {self.salary} and Role is {self.role}."

elon_musk = Ceo()
sunder_pichai = Ceo()

elon_musk.name = "Elon Musk"
elon_musk.salary = 809890
elon_musk.role = "Increase productivity of Employees"

sunder_pichai.name = "Sunder Pichai"
sunder_pichai.salary = 9987786
sunder_pichai.role = "Make problem solving product which is best"

print(elon_musk.details())
print(sunder_pichai.details())


# CONSTRUCTUR IN OOPS PROGRAMMING

class co_founder:
    def __init__(self, cname, ccompany, cachievement):
        self.name = cname
        self.company = ccompany
        self.achievement = cachievement

bill_gates = co_founder("Bill Gates", "Microsoft", "Most used OS in the World and on of the Richest Billionarie")
mark_zukerberg = co_founder("Mark Zukerberg", "Facebook", "Most Visited Social Networking site in the World and youngest Billionarie in the world")

print(bill_gates.name, bill_gates.company, bill_gates.achievement)
print(mark_zukerberg.name, mark_zukerberg.company, mark_zukerberg.achievement)

# CLASS METHOD IN OOPS PROGRAMMING

class actor:
    no_of_films = 10

    @classmethod # DECORATORS
    def change_no_of_films(cls, newfilms):
        cls.no_of_films = newfilms

prabhash = actor()
sarukh_khan = actor()

prabhash.change_no_of_films(53)
sarukh_khan.change_no_of_films(89)

# It changes the value of Class Variable not instance variable

print(prabhash.no_of_films)
