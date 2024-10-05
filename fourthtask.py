#author:alvin austin
#date:05-10-24
#Python program that uses functions from the math module to perform the following operations on a number provided by the user
import math
num1=int(input("Enter a number: "))
root=math.sqrt(num1)
facter=math.factorial(num1)
expo=math.pow(num1,2)
print("The suare root of the entered number is:",root)
print("the factorial of the entered number: ",facter)
print(num1,"raised to the power 2 is:",expo)