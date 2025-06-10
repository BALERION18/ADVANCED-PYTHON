"""a=int(input("enter no. 1= "))
b=int(input("enter no. 2= "))
c=int(input("enter no. 3= "))
z=a+b+c
print(z)


age=int(input("enter age: "))
if age>=18:
    print("you can vote")
    print("congrats")


num=int(input("enter a no. "))
sum=0
while sum > 0:
    sum = sum+num
    num=num-1
print("the sum is: ",sum)


n = [2,4,5,6,8,11,14,25,27,31]
for x in n:
    i=1;
    flag=0
    while i <= x:
        if x%i ==0:
            flag=flag+1
        i=i+1;
    if flag ==2:
        print(x)

# Function ==>

def findsum(a,b):
    result=a+b
    return result

x=5
y=7
z=findsum(x,y)
print(z)"""
from functools import reduce


# Positional argument
def fn(fname,lname):
    print(f"my first name is {fname} and last name is {lname}")
fn("rohan","singh")

#keyword argument
def fn(fname,lname):
    print(f"my first name is {fname} and last name is {lname}")
fn(lname="singh",fname="mohit")

#Default argument
def fn(fname,lname="singh"):
    print(f"my first name is {fname} and last name is {lname}")
fn("mohit")


def sum_num(num1,*num):
    result=num1
    for i in num:
        result +=i
    return result

r=sum_num(10,20,30)
print(f"sum of no. is {r}")

#variable length keyword argument
#def fn(**name):

result=lambda num1,num2,num3: num1+num2+num3
print(result(10,5,5))

#filter
numbers=[1,2,3,4,5,6,7,8,9]

def is_even(n):
    if n%2==0:
        return True

even_number=filter(is_even,numbers)
even_number_list=list(even_number)
print(even_number_list)

#by lambda
numbers=[1,2,3,4,5,6,7,8,9]

even_numbers = filter(lambda n: n%2==0,numbers)

even_number_list=list(even_numbers)
print(even_number_list)

#reduce()
from functools import reduce
num_list=[20,12,52,22,72,19,7]
large=reduce(lambda x,y:x if x>y else y, num_list)
print(large)

from functools import reduce
num_list=[20,12,52,22,72,19,7]
min=reduce(lambda x,y:x if x<y else y, num_list)
print(min)