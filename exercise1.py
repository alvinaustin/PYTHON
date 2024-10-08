#author:Alvin Austin
#date:8-10-24
#Write a Python program that performs the following tasks:userinput,addition,subtraction,multiplication,division,combined arithmetic operation
num1: int=int(input("Enter a 1st number : "))
num2=int(input("Enter a 2nd number : "))
num3=int(input("Enter a 3rd number : "))
summation=num1+num2
print("The sum of num1 and num2 is: ", summation)
subtraction=num2-num1
print("The difference when num2 is subtracted from num1 is: ", subtraction)
multiplication=num1*num2
print("The product of num1 and num2 is: ", multiplication)
if num2==0:
    print("Division by 0 is not defined")
else:
    division=num1/num2
    if num2==0:
        print("Division by 0 is not defined")
    else:
       modulus=num1%num2
combine_result=(num1 + num2)*num3/2
print("The result of (num1 + num2) * num3 / 2 is: ",combine_result)

