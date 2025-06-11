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
print(p)


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


# constructor
# def __init__(self):
    #body of constructor

# type of constructor
#1.Default
#2.Parameterized

#constructor xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
class student:
     def __init__(self):
        print("default constructor called")
     def __init__(self,name,marks,age):
         self.name=name
         self.marks=marks
         self.age=age
         print("parameterized constructor called")
     def show_info(self):
         print("name",self.name)
         print("marks",self.marks)
         print("age",self.age)

     def __del__(self):
         print("destructor called")

s1=student()
s2= student("rohit",95.5,19)
s1.show_info()
s2.show_info()"""



class student:
    def __init__(self, name=None, marks=None, age=None):
        if name is None and marks is None and age is None:
            print("default constructor called")
        else:
            self.name = name
            self.marks = marks
            self.age = age
            print("parameterized constructor called")

    def show_info(self):
        if hasattr(self, 'name'):
            print("name:", self.name)
            print("marks:", self.marks)
            print("age:", self.age)
        else:
            print("No student info to show.")

    def __del__(self):
        print("destructor called")


s1 = student()  # Calls default constructor
s2 = student("rohit", 95.5, 19)  # Calls parameterized constructor

s1.show_info()
s2.show_info()



class addition:
    first=0
    second=0
    answer=0
    def __init__(self, f, s):
        self.first=f
        self.second=s
    def display(self):
        print("first number = ",self.first)
        print("second number = ",self.second)
        print("addition = ",self.answer)
    def calculate(self):
        self.answer = self.first + self.second

obj = addition(1000,2000)
obj.calculate()
obj.display()


#more than one constructor hai to last wala hi call hota upr wale neglected

#inbuilt functions
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

#create an instance of a person
person = person("alice",30)

#use getattr to get attributes value
name = getattr(person, "name")
print(f"name:{name}") #output is alice

#use setattr to set value of attribute
setattr(person, "age",31)
print(f"updated age:{person.age}")  #output : updated age = 31

#use hasattr to check if an attribute exist
has_name = hasattr(person,"name")
print(f"has attribute 'name': {has_name}")   # output:has attribute 'name' :true

#use delattr to delete an attribute
delattr(person,"age")

#check if an attribute 'age' still exist after deleteion
has_age = hasattr(person,"age")
print(f"has attribute 'age' after deleteion {has_age}")


#pillars of oops
# encapsulation
# abstraction
# polymorphism
# inheritance


#exs
class employee:
    def __init__(self, name=None, posn=None, age=None):
        if name is None and posn is None and age is None:
            print("default constructor called")
        else:
            self.name = name
            self.posn = posn
            self.age = age
            print("parameterized constructor called")

    def show_info(self):
        if hasattr(self, 'name'):
            print("name:", self.name)
            print("posn:", self.posn)
            print("age:", self.age)
        else:
            print("No employee info to show.")

    def __del__(self):
        print("destructor called")


s1 = employee()  # Calls default constructor
s2 = employee("rohit", "CMO", 24)  # Calls parameterized constructor

s1.show_info()
s2.show_info()



#exs
class Addition:
    # Class attribute
    multiplier = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute(self):
        result = self.x  + self.y
        return result * Addition.multiplier
    

#  class attribute
Addition.multiplier = 2

#  instance
add = Addition(5, 3)
print(add.compute()) 



