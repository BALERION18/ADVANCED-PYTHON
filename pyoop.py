"""# for strings
st='10'
x=st+'s'
print(x)

st='100'
x =st.__add__('s')
print(x)"""


# program for making magic_method
class Mass:
    def __init__(self, kg=0, g=0):
        # ensure grams are less than 1000
        self.kg = kg + g // 1000
        self.g = g % 1000

    def __add__(self, other):
        # add kg and g separately
        total_kg = self.kg + other.kg
        total_g = self.g + other.g

        # if g exceed 1000, convert to kg
        if total_g >= 1000:
            total_kg += total_g // 1000
            total_g = total_g % 1000  # corrected this line

        return Mass(total_kg, total_g)

    def __repr__(self):
        return f"{self.kg} kg and {self.g} g"


# Example
mass1 = Mass(2, 500)
mass2 = Mass(1, 750)
mass3 = mass1 + mass2
print(mass3)


class Distance:
    def __init__(self, km=0, m=0):
        self.km = km + m // 1000
        self.m = m % 1000

    def __add__(self, other):
        total_km = self.km + other.km
        total_m = self.m + other.m

        if total_m >= 1000:
            total_km += total_m // 1000
            total_km = total_m % 1000

        return Distance(total_km, total_m)

    def __repr__(self):
        return f"{self.km} km and {self.m} m"


# example =
dis1 = Distance(2, 500)
dis2 = Distance(1, 750)
dis3 = dis1 + dis2
print(dis3)


class Distance:
    def __init__(self, km=0, m=0):
        # ensure grams are less than 1000
        self.km = km + m // 1000
        self.m = m % 1000

    def __add__(self, other):
        # add kg and g separately
        total_km = self.km + other.km
        total_m = self.m + other.m

        # if g exceed 1000, convert to kg
        if total_m >= 1000:
            total_km += total_m // 1000
            total_m = total_m % 1000  # corrected this line

        return Distance(total_km, total_m)

    def __repr__(self):
        return f"{self.km} km and {self.m} m"


# Example
dis1 = Distance(2, 500)
dis2 = Distance(1, 750)
dis3 = dis1 + dis2
print(dis3)


# which is greater
class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


s1 = student(58, 69)
s2 = student(69, 65)
if s1 > s2:
    print("s1 is greater")
else:
    print("s2 is greater")


# __str__()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return F"the name is {self.name} and age is {self.age}"


p = Person("mohit", 30)
print(p)

# __new__  (allocate memory for attribute)


import math


class fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        common_divisor = math.gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.denominator * self.denominator
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.numerator < other.numerator * self.denominator

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"


f1 = fraction(1, 2)
f2 = fraction(2, 3)
f3 = f1 + f2
print(f3)
print(f1 == f2)


#instance as an argument
class myclass:
    def __init__(self,value):
        self.value=value

def print_value(obj):
        print(f"the value is: {obj.value}")

obj=myclass(10)
print_value(obj)


#obj as an argument
class Person:
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return f"Person({self.name})"

class Greetings:
    def generate_greeting(self,person):
        return f"hello,{person.name}! welcome!"

person=Person("alice")
greeting=Greetings()

message=greeting.generate_greeting(person)
print(message)

#instances as return values
class Myclass:
    def __init__(self,value):
        self.value=value

def create_object(value):
    return Myclass(value)

obj=create_object(10)
print(obj.value)


#
"""class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height

    def combine(self,other):
        new_width=self.width
        new_height=new_area/new_width
        return rectangle(new_width,new_height)

    def __repr__(self):
        return f"rectangle({self.width},{self.height}"


rect1=rectangle(4,5)
rect2=rectangle(3,6)

combined_rect=rect1.combine(rect2)
print(combined_rect)"""


#namespace
def my_func():
    a=5
    b=15
    c=20
    print("in local")
    print(dir())
    def inner():
        a=5
        print("in inner")
    inner()
    print(dir())
my_func()


def outer_function():
    x=20


    def inner_function():
        print(x)
    inner_function()
    print(dir())

outer_function()
print(dir())


x=50

def my_func():
    print(x)

my_func()
print(x)
print(dir())


print(len([1,2,3]))


#day4

# abstraction, encapsulation, inheritance, polymorphism =

# abstraction = process of hiding unnecessary details from user. eg = food order apps
# encapsulation = process of binding data(variable) and methods into a class
# inheritance = process by which class acquires data from parent class
# polymorphism = ability to have different methods with same name but perform task

# Inheritance
class parent:
    def feature1(self):
        print("feature 1 f parent")

    def feature2(self):
        print("feature 2 of parent")

class child(parent):
    def feature3(self):
        print("feature 3 f parent")

    def feature4(self):
        print("feature 4 of parent")

p=parent()
p.feature2()

c=child()
c.feature1()

class Animal:
    name=""
    def eat(self):
        print("i can eat")

class Dog(Animal):
    def display(self):
        print("my name is",self.name)

labrador=Dog()
labrador.name="rohu"
labrador.eat()
labrador.display()

class father:
    money=1000
    def show(self):
        print("parent class instance method")
    @classmethod
    def moneyshow(cls):
        print("parent class method: total money = ",cls.money)
    @staticmethod
    def stat_method(father):
        a=5
        print("parent class static method: value of a is ",a)

class son(father):
    def son_display(self):
        print()











# super
class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print("first name is {} and last name is {}".format(self.fname,self.lname))
class student(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        print("inside student class init")

s = student("mohit","raj")

#is subclass
class father:
    pass
class son(father):
    pass
print(issubclass(son,father))


class student:
    _name= None
    _roll= None
    _branch= None

    def __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch

    def _displayinfo(self):
        print("roll: ",self._roll)
        print("Branch: ",self._branch)

class learnowx(student):
    def __init__(self,name,roll,branch):
        student.__init__(self,name,roll,branch)

    def displaydetails(self):
        print("name: ",self._name)
        self._displayinfo()

obj=learnowx("aditya",101203,"ds")
obj.displaydetails()

#private-method
class student:
    _name= None
    _roll= None
    _branch= None

    def __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch

    def _displayinfo(self):
        print("name: ",self._name)
        print("roll: ",self._roll)
        print("Branch: ",self._branch)

    def accessprivatemethod(self):
        self._displayinfo()

    def displaydetails(self):
        print("name: ",self._name)
        self._displayinfo()

obj=student("adi",101200,"me")
obj.accessprivatemethod()

#day5

#duck typing
class Duck:
    def quack(self):
        print("Quack!")
class Person:
    def quack(self):
        print("I'm quacking like a duck!")
class eat:
    def quack(self):
        print("quack is eating")
# Both Duck and Person can be passed to make_it_quack
duck = Duck()
person = Person()
eating=eat()

duck.quack()         # Output: Quack!
person.quack()       # Output: I'm quacking like a duck!
eating.quack()

class Student:
     def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
# overloading the + operator
     def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

s1 = Student("raj", "singh")
s2 = Student("ram", "verma")
s3 = s1 + s2
print(s3.m1)


class Vector:
    def __init__(self, x, y):  # Corrected constructor
        self.x = x
        self.y = y

    def __add__(self, other):  # Corrected addition
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # Corrected subtraction
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # Corrected multiplication (dot product)
        return self.x * other.x + self.y * other.y

    def __str__(self):  # Corrected string representation
        return f"({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2
v4 = v1 - v2
dot_product = v1 * v2

print("v1:", v1)
print("v2:", v2)
print("v1 + v2:", v3)
print("v1 - v2:", v4)
print("v1 * v2 (dot product):", dot_product)



def outerFunction(text):
    text=text
    def innerFunction():
        print(text)
    return  innerFunction
myFunction=outerFunction("Hey!")
myFunction()

"""#Decorator(self made)
def decor(addition):
    def inner():
        result=addition()  #existing function calling
        num3=int(input("Enter no. 3:"))
        result=result+num3
        print("result",result)

    return inner   #closure
@decor
def addition():
    num1=int(input("enter no. 1: "))
    num2=int(input("enter no. 2: "))
    result=num1+num2
    return result


addition()

def decor(func):
    def inner():
        print("-----------------------")
        func()
        print("-----------------------")
    return inner

@decor
def msg():
    print("python programming")

msg()"""

#current time code
from  datetime import datetime

def not_during_night(func):
    def inner():
        if 7<= datetime.now().hour<22:
            func()
        else:
            print("sorry! cant play at night")
    return inner

@not_during_night
def music():
    print("playing music")

music()

#
def do_twice(func):
    def wrapper_do_twice(*args, **kargs):
        func(*args, **kargs)
        func(*args, **kargs)
    return wrapper_do_twice

@do_twice
def msg(name):
    print(f"hello {name}")

msg("mohit")

# returning value from decorated fn
def do_twice(func):
    def wrapper_do_twice(*args, **kargs):
        func(*args, **kargs)
        return func(*args, **kargs)
    return wrapper_do_twice

@do_twice
def msg(name):
    return(f"hello {name}")

text=msg("mohit")
print(text)

# multiple decorator
def decor1(func):
    def inner():
        x=func()
        return x*x
    return inner
def decor(func):
    def inner():
        x=func()
        return 2*x
    return inner
@decor1
@decor
def num():
    return 10
print(num())


#genrator of numbers b/w 1-10

def generate_numbers():
    for num in range(1,11):
        yield num

numbers_generator=generate_numbers()
print(type(numbers_generator))

for number in numbers_generator:
    print(number)


# Immutable tuple
coordinates=(10,20)
#any attempt to modify will create new tuple
new_coordinates=coordinates+ (30,)

print(coordinates)
print(new_coordinates)

#coroutines
from time import sleep
students = ["atul","naveen","mayank","rakhi","anmol","neha","ayush"]
def read():
    sleep(3)
    print("Reading done....")
    data=students
    while True:
        name = (yield)  #execution suspend
        if name in data:
            print("found")
        else:
            print("not found")

search=read()
print("Reading all data.....")
next(search)
search.send("ayush")
search.send("atul")


#2
def print_name(prefix):
    print("Searching prefix: {}".format(prefix))
    while True:
        name=(yield)
        if prefix in name:
            print(name)


corou = print_name("Dear")


corou.__next__()

corou.send("Atul")
corou.send("Dear Atul")


#doubt
#when you create iterator it returns itself
l=[5,8,7,3,6,2]
iter_obj1=iter(l)
iter_obj2=iter(l)
print("id of iter_obj1: ",id(iter_obj1))
print(type(iter_obj1))
print("id of iter_obj1",id(iter_obj1))

print("id of iter_obj2: ",id(iter_obj2))
print(type(iter_obj2))
print("id of iter_obj2",id(iter_obj2))

#create own for loop using iterator
lt=[52,12,17,23,37,44]

def my_for_loop(iterable):
    iterator=iter(iterable)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        pass
my_for_loop(lt)

#own range function
class my_range:
    def __init__(self, start=0, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return my_range_iterator(self)


class my_range_iterator:
    def __init__(self, iterable_obj):
        self.current = iterable_obj.start
        self.stop = iterable_obj.stop
        self.step = iterable_obj.step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        result = self.current
        self.current += self.step
        return result


# Usage
num = my_range(1, 10)  # behaves like range(1, 10)
for n in num:
    print(n)

