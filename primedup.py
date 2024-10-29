limit=int(input("how many prime number to be shown"))
for number in range(2,limit+1):
    is_prime=True
    for i in range(2,(number//2)+1):
        if number%i==0:
            is_prime=False
            break
    if is_prime:
       print(number)