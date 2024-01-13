ans = [1,1,2,2,2,8]
inp = input().split()
inp = list(map(int,inp))
[print(ans[i] - inp[i] , end=" ") for i in range(6)]
