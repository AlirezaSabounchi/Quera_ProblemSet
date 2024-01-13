num = list(map(int ,input().split()))
temp = [0,0,0,0]
if num[0] == 0 :
    [print(int(i),end=" ") for i in temp]
    quit()
if min(num[0],num[2]) == num[0] :
    temp = [((2*num[0])-1)//4]*4
    if ((2*num[0])-1)%4 != 0 :
        for i in range(((2*num[0])-1)%4) :
            temp[i] += 1
if min(num[0],num[2]) == num[2] :
    temp = [(2*num[2])//4]*4
    if (2*num[2])%4 != 0 :
        for i in range((2*num[0])%4) :
            temp[i] += 1
    if num[2] == 0 and num[0] != 0 :
        temp[0] += 1
[print(int(i),end=" ") for i in temp]
