inp = []
inp = list(map(float , input().split()))
for i in range(0,int((inp[0]//inp[2])) +1) :
    a = (inp[0]-(i*inp[2])) / inp[1]
    if int(a) == a :
        print(int(a),i)
        quit()
print("-1")
