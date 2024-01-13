inp = list(input())
out = []
leng = len(inp)
for i in range(len(inp)) :
    out.append("".join(i*inp[i]) + "".join(inp[i:leng]))
    print(out[i])
