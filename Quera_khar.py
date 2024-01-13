import math
inp = input().split()
inp = [int(i) for i in inp]
if inp[2] % 2 == 0 :
    time = int((inp[2] / 2) * (inp[0]+inp[1]))
else :
    time = int(math.ceil(inp[2] / 2) * (inp[0]) + math.floor(inp[2] / 2) * (inp[1]))
print(time)
