num = input()
num = int(num)
sum = 0
for i in range(num):
    if i!= 0 and num % i == 0 :
        sum += i
if sum == num :
    print("YES")
else :
    print("NO")
