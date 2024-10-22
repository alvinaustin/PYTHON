#author=Alvin Austin
#date=22-10-24
#Write a Python program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the numbers.
temp = float(input("Enter Temperature:"))
corf = input("is this (C)elsius or (F)ahrenheit?")
if corf=='C':
    c="Celsius"
else:
    c="Fahrenheit"
ctemp=0
if corf=="C":
    f="Fahrenheit"
    ctemp=(9/5*temp)+32
else:
    f="Celsius"
    ctemp=5/9*(temp-32)

print(temp,c,"is",ctemp,f)

