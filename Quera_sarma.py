inp = []
temp = []
for i in range(5) :
    inp.append(input())
    if "HAFEZ" in inp[i] or "MOLANA" in inp[i] :
        temp.append(i+1)
if sum(temp)==0 :
    print("NOT FOUND!")
else :
    print(temp)
