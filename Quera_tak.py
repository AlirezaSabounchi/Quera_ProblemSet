def single (num):
    sum = 0
    while True :
        if num > 10 :
            temp = num % 10
            sum += temp
            num = num // 10
        elif num == 10 :
            sum += 1
            return(sum)
            break
        else :
            sum += num
            return(sum)
            break
if __name__ == "__single__" : single()
###
num = input()
num = int(num)
if num >= 10 :
    while num > 9 :
        num = single(num)
    print(num)
else : print(num)
