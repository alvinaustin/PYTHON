input1=int(input("How many elements in First List"))
input2=int(input("How many elements in Second List"))
lst1=[]
lst2=[]
for i in range (input1+1):
    num1=int(input("Enter Elements of first list"))
    lst1.append(num1)

for j in range (input2+1):
    num2=int(input("Enter Elements of second list"))
    lst2.append(num2)


print(lst1)
print(lst2)
lst1_even=[]
lst1_odd=[]


for numb in lst1:
  if numb%2==0:
    lst1_even.append(numb)
  else:
      lst1_odd.append(numb)

lst2_even=[]
lst2_odd=[]



for num in lst2:
  if num%2==0:
   lst2_even.append(num)
  else:
      lst2_odd.append(num)



lst1_even.extend(lst2_even)
lst1_odd.extend(lst2_odd)

lst1_even.sort()
lst1_odd.sort()

lst1_even.extend(lst1_odd)
print(lst1_even)










