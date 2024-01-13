inp = list()
while True :
    num = input()
    if num != "0" :
        inp.append(num)
    elif num == "0" :
        break
[print(i) for i in inp[::-1]]
