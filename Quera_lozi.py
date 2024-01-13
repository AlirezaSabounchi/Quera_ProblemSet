inp = int(input())
for i in range(1,inp+1,2) :
    print(int(((inp-i)/2)) * " " , i * "*" , int((inp-i)) * " " , i * "*" , int(((inp-i)/2)) * " " , sep="")
for i in range(inp-2,0,-2) :
    print(int(((inp-i)/2)) * " " , i * "*" , int((inp-i)) * " " , i * "*" , int(((inp-i)/2)) * " " , sep="")
