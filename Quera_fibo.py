def fib(n) :
    fibo = []
    fibo[0:3] = [0,1,1]
    if n < 3 :
        return fibo[1:n+1]
    if n > 2 :
        for i in range(3,n+1) :
            fibo.append(fibo[i-1] + fibo[i-2])
    return fibo
inp = int(input())
fibo = fib(inp)
for i in range(1,inp+1) :
    if i in fibo :
        print("+" , end="")
    else :
        print("-" , end="")
