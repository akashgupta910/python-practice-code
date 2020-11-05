# SINGLE and MULTIPLE INHERITANCE

class Employee:
    def __init__(self, name, work, salary):
        self.name = name
        self.work = work
        self.salary = salary

    def printemp(self):
        return f"The Employee Name is {self.name}. Work is {self.work} and Salary is {self.salary}."

class Player:
    def __init__(self, name, work, salary, sports):
        self.name = name
        self.work = work
        self.salary = salary
        self.sports = sports

    def printplayer(self):
        return f"The Player Name is {self.name}. Work is {self.work} and Salary is {self.salary} and Mastery in {self.sports} sports."

class cool_Employee(Employee, Player):
    def __init__(self, name, work, salary, sports, languages):
        self.name = name
        self.work = work
        self.salary = salary
        self.sports = sports
        self.language = languages

    def printpro(self):
        return f"The Programmer Name is {self.name}. Work is {self.work} and Salary is {self.salary}.Play {self.sports} Sports and Mastery in {self.language} languages."


qazi = Player("Rehan Qazi","Teach sports",10000,["Cricket","Football","Basket Ball"])
randy = Employee("Randy Ortan","Teach Wrestling",20000)\

warren = cool_Employee("Warren Buffet","Investing",15000,["Basket Ball","Tennis"],["Python","C++"])

print(qazi.printplayer())

print(randy.printemp())

print(warren.printpro())


