n , temp = [] , 0
n = input().split()
n = list(map(int,n))
for i in range(n[0]) :
    temp += int(input())
if n[1] > temp :
    print("NO")
else :
    print("YES")
