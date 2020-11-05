"""
Encapsulation:-

    In an object oriented python program, you can restrict access to methods and variables.
    This can prevent the data from being modified by accident and is known as encapsulation.

Abstraction:-

    abstraction is a method to hide internal functionalities from user.

Polymorphism:-

    Ability to take various Form.
    Ex:- print(5+6) = 11
         print("5" + "6") = 56

Inheritance:-

Use the all function of one class into another class and add more features.
ex:- Parents ke gunn bachhe mein.

    Single Inheritance:-
        ex:- class Employee:
                ..........
             class Programmer(Employee):
                ..........
    Multiple Inheritance:-
        ex:- class Employee:
                .........
             class Player:
                .........
             class Coolprogrammer(Employee, Player):
                .........
    Multilevel Inheritance:-
        ex:- class Dad:
                ......
             class Son(Dad):
                ......
             class Grandson(Son):
                ......

Public, Protected and Private Acess specifiers:-
    ex:-
        public:- str = "Hello"
        protected: _str = "Hello"
        private: __str = "Hello" (To access this use: _Classname__str [This is name mangling])

Super() and Overriding:-
    ex:-
        class B(A):
            def __init__(self):
                super().__init__()
                self.var1 = "Hello"
                self.var2 = "World"

Diamond Shape Problem In Multiple Inheritance:-

Operator Overloading and Dunder Method:-
    Dunder Method - Method which starts with double underscore(__). ex; __init__. Also called special Method.

    Ex:- def __add__(self, other):
            return self.salary + other.salary

Abstract Method:- (@abstractmethod)
    Aisha method jisse sabhi ko define karni hai.

Setters and Property Decorators:-
    property:- (you don't need to call as a function)
                Ex:- @property
                     def email(self):
                        ......
                     email

Object Introspection:-
    kisi bhi object ke baare mein jannna.
    Ex:- print(type(...))
         print(id(...))
         print(dir(...))

"""