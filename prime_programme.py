# Here your code goes.....
def prime(num):
    if num<=1:
        return False
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True
print(prime(int(input('Please Enter the number :'))))