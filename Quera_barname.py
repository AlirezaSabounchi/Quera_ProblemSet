num = input()
inp = input().split()
temp = []
for i in range(len(inp)) :
    temp.append(inp[len(inp)-i-1])
temp = " ".join(temp)
print(temp)
