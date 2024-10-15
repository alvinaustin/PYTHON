# author=Alvin Austin
# date=15-10-24
num=int(input("Enter number of which factorial is wanted: "))
fact=1
if num<0:
    print("Enter positve integer")
elif num==0:
    print("Factorial of 0 is 1 ")
else:
    for i in range (1,num+1):
     fact=fact*i

print("factorial of the number is:,",fact)