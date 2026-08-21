from os import name
class Employee:
    companyName="KodNest"

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def printDetails(self):
        print(Employee.companyName)
        print(self.name)
        print(self.id)

e1=Employee("Arun",11)
e2=Employee("Rana",22)
e1.printDetails()
e2.printDetails()
print("----------")

Employee.companyName="KodNest Tech"
e1.printDetails()
print(e1.companyName)
print(e2.companyName)
print("------")

e1.companyName="xyz"
e1.printDetails()
e2.printDetails()
print("------------")
print(e1.companyName)
print(e2.companyName)
print(Employee.companyName)