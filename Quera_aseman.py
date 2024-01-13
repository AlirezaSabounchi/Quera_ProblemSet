n = int(input().split()[0])
temp , line = [[],[]]
for i in range(n) :
    line = input()
    temp.append(line.count("*"))
print(sum(temp))
