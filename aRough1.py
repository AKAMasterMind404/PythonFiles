# import numpy
class Employee:
    def __init__(self, ID, Name, Phone, Age, Gender, Department, Salary):
        self.id = ID
        self.name = Name
        self.phone = Phone
        self.age = Age
        self.gender = Gender
        self.department = Department
        self.salary = Salary

    def printinfo(self):
        printinfo = ([self.id, self.name, self.phone, self.age, self.gender, self.department, self.salary])
        print(printinfo)


e1 = Employee(1, "Atharv", 8668692436, 20, "Male", "CEO", 200000000)
print(e1.printinfo())
