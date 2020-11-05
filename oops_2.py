class Employee:
    no_of_employee = 0

    def details(self):
        return f"The Employee Name is {self.name} and the Work is {self.work}."

    def __init__(self , name, work):  # THIS IS CONSTRUCTUR IN OOPS PROGRAMMING IN PYTHON
        self.name = name
        self.work = work

    @classmethod
    def change_no_of_employee(cls, new_employee):
        cls.no_of_employee = new_employee

    # CLASS METHOD AS ALTERNATIVE CONSTRUCTORS
    @classmethod
    def from_slash(cls, string):
        # employee_string = string.split("/")
        # return cls(employee_string[0],employee_string[1])
        # OR ->>>
        return cls(*string.split("/"))  # THIS IS *ARGS



harry = Employee("Harry","Programming")
carry = Employee("Carry Minati","Make Roating videos")
qazi = Employee.from_slash("Rehan Qazi/Programming")

harry.change_no_of_employee(20)
carry.change_no_of_employee(89)

# harry.name = "Harry"
# harry.work = "Programming"
#
# carry.name = "Carry Minati"
# carry.work = "Make Roasting videos"
#
# harry.no_of_employee = 2
# carry.no_of_employee = 5

print(qazi.work)

# print(harry.name)
# print(harry.no_of_employee)
# print(Employee.no_of_employee)
# print(carry.no_of_employee)

# print(Employee.no_of_employee)

# print(harry.name)
# print(carry.work)
# print(harry.details())

# STATIC METHOD IN OOPS PROGRAMMING

class workers:

    @staticmethod
    def who_is_good(string):
        print(f"{string} is a Good Boy")

Larry = workers()

workers.who_is_good("Harry")
Larry.who_is_good("Ajey")

