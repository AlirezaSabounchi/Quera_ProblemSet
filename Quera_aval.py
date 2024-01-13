def isprime(n):
    if n==0 or n==1 :
        return False
    for i in range(2,n) :
        if n%i == 0 :
            return False
    return True

first = int(input())
last = int(input())
[print (i) for i in range(first,last+1) if isprime(i) ]
