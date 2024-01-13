from collections import Counter
temp , pos , x , y  = [],[],[],[]
for i in range(3) :
    pos.append(input().split())
    x.append(pos[i][0])
    y.append(pos[i][1])

[print(k , end=" ") for k,v in Counter(x).items() if v == 1]
[print(k) for k,v in Counter(y).items() if v == 1]
