class Persons:
    def __init__(self, name, address):
        self.name=name
        self.address=address
    
class Employee(Persons):
    def __init__(self,name, address,salary):
        super().__init__(name, address)
        self.salary=salary
        
    def display(self):

        print("Employee name: ",self.name)
        print("Employee address: ",self.address)
        print("Employee salary: ",self.salary)
        print("------------------------------")
n=int(input("Enter number of employees to be entered :"))
obj=[] 
for i in range(n):       
    n=input("Enter name of employee :")
    add=input("Enter address of employee :")
    s=input("Enter salary of employee :")
    
    obj.append(Employee(n, add, s))
print("Employee details")
for e in obj:
    e.display()

