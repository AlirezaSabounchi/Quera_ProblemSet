list_degree = [0,0,0]
list_degree = input().split()

for i in [0,1,2,] :
    list_degree [i] = int(list_degree [i])

total = 0
redflag = 0
for i in [0,1,2] :
    if list_degree[i] != 0 :
        total = total + list_degree[i]
    else :
        redflag = 1

if total == 180 and redflag == 0 :
    print("Yes")
else :
    print("No")
