import math
count,n,temp=0,int(input()),0
for i in range(1,n+1) :
    if math.floor(n//i) == n//i :
        count += n//i
        temp += (n//i)*i
print(count,temp)
