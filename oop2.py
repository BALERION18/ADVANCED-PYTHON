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