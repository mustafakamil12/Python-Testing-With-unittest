# Python program to demonstrate
# use of a class method and static method.

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age >= 18

# Creating an instance using the constructor
person1 = Person('Mayank', 21)

# Creating an instance using the class method
person2 = Person.fromBirthYear('Mayank', 1996)

print(f"Person1 Age: {person1.age}")
print(f"Person2 Age: {person2.age}")

# Checking if person1 is an adult
print(f"Is Person1 an adult? {'Yes' if Person.isAdult(person1.age) else 'No'}")

# Checking if person2 is an adult
print(f"Is Person2 an adult? {'Yes' if Person.isAdult(person2.age) else 'No'}")