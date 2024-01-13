num = int(input())
inp = []*num
inp = list(map(float,input().split()))
print(inp.index(max(inp))+1)
