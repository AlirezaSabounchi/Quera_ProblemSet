import math
temp = 0
inp = []
start = int(input())
fin = int(input())
for i in range (start+1 , fin) :
    for j in range(2,int(math.sqrt(i))+1) :
        if i%j == 0 :
            temp += 1
    if temp == 0 :
        inp.append(str(i))
    temp = 0
print(",".join(inp))
