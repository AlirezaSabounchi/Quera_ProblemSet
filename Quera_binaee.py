leng = int(input())
inp = list(input())
test = list(input())
j = 0
for i in range(leng) :
    if inp[i] != test[i] :
        j += 1
print(j)
