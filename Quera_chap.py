num = input()
length = len(num)
num = int(num)
temp = num
count = 0

while temp != 0 :
    temp //= 10
    count += 1
if num == 0 :
    count = 1

list_num = [0]*count

for i in range(count) :
    if num <= 9 and num >= 0 :
        list_num [i] = num
        break
    elif num > 9 :
        list_num[i] = num % 10
        num =  num // 10

list_num.reverse()
if length > count :
    dif = length - count
    list = [0]*dif
    list_num = list + list_num
    count += dif
    
for i in range(count) :
    print('{}:'.format(list_num[i]) , end=" ")
    for j in range(list_num[i]) :
        print(list_num[i] , end="")
    print("")
