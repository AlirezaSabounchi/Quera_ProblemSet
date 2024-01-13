n = 2*int(input())+1
[print(int(((n-i)/2))*" " , i*"*" , sep="") for i in range(1,n,2)]
[print(int(((n-i)/2))*" " , i*"*" , sep="") for i in range(n,0,-2)]
