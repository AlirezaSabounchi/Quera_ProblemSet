inp = int(input())
temp = [0]*(inp+1)
temp[1] = 1
for i in range(1 , inp+1) :
    for j in range(i , 0 , -1) :
        temp[j] = temp[j] + temp[j-1]
    print(" ".join(str(x) for x in (temp[1:i+1])))
