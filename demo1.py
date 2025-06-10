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
print("the sum is: ",sum)"""


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