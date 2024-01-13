import math
inp = input().split()
temp = int(inp[0])
for i in range(int(inp[1])) :
    temp = math.floor(temp/2)
print(temp)
