num,temp =[],[]
for i in [0,1,2,3,4,5] :
    num.append(int(input()))
    if i%2==1 :
        temp.append(min(num[i-1],num[i]))
print(sum(temp))
