#author=Alvin Austin
#date=15-10-24

num1=int(input("Enter a Number"))
num2=int(input("Enter a Number"))
num3=int(input("Enter a Number"))
if num1>num2 and num1>num3:
    print("the greatest number is",num1)
elif num2>num1 and num2>num3:
    print("the greater number is",num2)
elif num3>num1 and num3>num2:
    print("the greater number is",num3)
else:
    print("num1num2=num3")
