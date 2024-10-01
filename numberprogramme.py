#this programme intakes a number and takes the sum of all number up until it reaches the entered number
#author:alvin austin
#date:01-10-24
input_number=int(input("enter till where the numbers should be added : "))
lst=[]
for i in range(1,input_number+1):
    lst.append(i)
sum_of_number=sum(lst)
print(sum_of_number)
