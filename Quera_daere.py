inp,temp = list(map(int,input().split())),[1]
if inp[0] < inp[1] :
    quit()
i = 0
while True :
    i += inp[1]
    if i >= inp[0] :
        i = i%inp[0]
    temp.append(i+1)
    if i == 0 and len(temp) > 2 :
        [print(len(temp)-1)]
        quit()
    elif i == 0 and len(temp)== 2 :
        [print("1")]
        quit()
    else :
        continue
