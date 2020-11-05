# OPERATOR OVERLOADING AND DUNDER METHOD

class Programmer:

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_programmer(self):
        return f"The Senior Programmer Name is {self.name}. Salary is {self.salary} and Role is {self.role}."

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mod__(self, other):
        return self.salary % other.salary

    def __repr__(self):
        return f"Repr - The Senior Programmer Name is {self.name}. Salary is {self.salary} and Role is {self.role}."

    def __str__(self):
        return f"Str - The Senior Programmer Name is {self.name}. Salary is {self.salary} and Role is {self.role}."



cs_dojo = Programmer("CS Dojo",25000,"Remove Bugs in sites")
qazi = Programmer("Rehan Qazi",22000,"Check Bugs in sites")
harry = Programmer("Harry",15000,"Improve coding of sites")

print(cs_dojo + qazi)
print(cs_dojo / qazi)
print(cs_dojo * qazi)
print(cs_dojo - qazi)
print(cs_dojo % qazi)



print(repr(cs_dojo))


