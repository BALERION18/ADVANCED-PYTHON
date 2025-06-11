"""class Apple_design:  #class design
    count = 0 #class variable or static variable
    def __init__(self , cpu, ram):  #constructor
        self.cpu = cpu
        self.ram = ram
    
    def mobile(self):  #instance variable
        print("this is phone 1")
        print(self.cpu, self.ram)
        

m1 = Apple_design(3.5, 8)
m2 = Apple_design(4.5, 16)
m1.mobile() #parameterized comstructor = jb argument pass krte
m2.mobile()
print(id(m1))
print(id(m2))


#create class and object example
class greetings:
    message="hello world"
    
    def say_hello(self):
        print(self.message)
        
# create object
greet = greetings()
greet.say_hello()


class car_design:
    Wheel = 4  #class variable
   
   
    def __init__(self, model, milage, year):
        self.model = model
        self.milage = milage
        self.year = year 
    
    def car_info(self):
        print("model no.", self.model)
        print("car milage.", self.milage)
        print("year.", self.year)
        print("wheel no.", self.Wheel)
        
car1 = car_design("Maruti", 22.5, 2018)
car2 = car_design("kia", 30, 2020)
car3 = car_design("hyundai", 28.5, 2021)
car1.car_info()
car2.car_info()
car3.car_info()


class computer:
    count = 0
    
    
    def __init__(self, company , cpu , ram):
        self.comapny = company
        self.cpu = cpu
        self.ram = ram
        
    def computers(self):
        print("company", self.comapny)
        print("model no.", self.cpu)
        print("ram", self.ram)
                
c1 = computer("dell", "i5", 8)
c2 = computer("lenovo", "i7", 16)
c1.computers()
c2.computers()


class Employee:
    office_name = "NIET"
    
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
    
    def show_details(self):
        print("name:", self.name)
        print("designation:", self.designation)
        print("office:", self.office_name)

# Create Employee instances correctly
e1 = Employee("rahul", "CEO")
e2 = Employee("ankit", "CTO")

e1.show_details()
e2.show_details()

# appending, if-else
class number:
    evens = []
    odds = []
    def __init__(self,num):
        self.num = num
        if num % 2 == 0:
            number.evens.append(num)
        else:
            number.odds.append(num)

n1 = number(32)
n2 = number(21)
n3 = number(43)
n4 = number(43)
n5 = number(54)
n6 = number(65)
n7 = number(47)
print("even no.s are:",number.evens)
print("odd no.s are:",number.odds)


# __str__
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return F"The name is {self.name} and age is {self.age}"
    
p = person("amit", 30)
print(p)"""


#Methods in Python

# 1. instance = by deafault every method is instance(self)
#(called by instance name)


# 2. class method
#@classmethod
#def_____(cls,arg1,__):
#    ---------------
#    ---------------
#(called by class,instance name)


# 3. static method
#@staticmethod
#def_____(arg1,arg2,__):
#    ---------------
#    ---------------
#(called by class name)

# class
class student:
    counter = 0
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        student.counter = student.counter + 1
    def msg(self):
        print("hello "+self.name + " you got ",self.marks, "% marks")
    @classmethod
    def object_count(cls):
        return cls.counter
s1=student("abhishekh",65)
s2=student("raj",20)
print(student.object_count())
print(s1.object_count())

        
#static
class mathoperation:
    @staticmethod
    def addnum(a,b):
        return a+b
    
    @staticmethod
    def subnum(a,b):
        return a-b
    
obj = mathoperation()
result_add=mathoperation.addnum(10,5)
result_sub=mathoperation.subnum(10,5)

print(f"addition: {result_add}")
print(f"subtraction: {result_sub}")

