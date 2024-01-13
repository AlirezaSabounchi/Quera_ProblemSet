days = dict()
num,day = [0,0,0],[]
for i in range(3):
    num[i] = input()
    day = input().split()
    for j in day:
        days[j] = days.get(j , 0)+1
print (7 - len(days.keys()))
