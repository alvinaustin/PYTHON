num=int(input("enter a number"))
is_prime=True
for i in range(2,num):
    if num%i==0:
        is_prime=False

if is_prime:
    print(f"The entered number {num} is prime")
else:
    print(f"the entered number {num} is not prime")