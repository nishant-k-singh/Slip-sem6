class Student:
    def __init__(self, rollno, name, age, gender):
        self.rollno=rollno
        self.name=name
        self.age=age
        self.gender=gender
class Test(Student):
    def __init__(self, rollno, name, age, gender,phy, chem, maths):
        super().__init__(rollno, name, age, gender)
        self.phy=phy
        self.chem=chem
        self.maths=maths
        
    def __str__(self):
        self.total=self.phy+self.chem+self.maths
        return f'''Roll no:{self.rollno} \nName:{self.name} \nAge:{self.age} \nGender:{self.gender}
Marks of Subjects:\nPhysics={self.phy} Chemistry={self.chem} Maths={self.maths}
Total Marks: {self.total}\n--------------------'''
    
t=Test(1, "Nishant", 20, "M",80,90,99)
t1=Test(2, "Olivia", 19, "F",75,95,85)
t2=Test(3, "Ayush", 18, "M",78,98,88)
print(t)
print(t1)
print(t2)