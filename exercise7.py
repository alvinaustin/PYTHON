# author=Alvin Austin
# date=15-10-24
num1=int(input("Enter number of students in class: "))
b_total=0
tbh=0
g_total=0
tgh=0
for i in range(0,num1):
    gender=input("Enter Gender")
    tall=int(input("Enter Height"))
    if gender=="m":
        b_total+=1
        tbh=tbh+tall
    else:
        g_total+=1
        tgh=tgh+tall


avg_bh=tbh/b_total
print(avg_bh)
avg_gh=tgh/g_total
print(avg_gh)