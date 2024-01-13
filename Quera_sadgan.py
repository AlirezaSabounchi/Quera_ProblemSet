num1 = list(input())
num2 = list(input())
for j in range(2,0,-1) :
    if num1[j]  > num2[j] :
        print("".join(num2) , "<", "".join(num1))
        break
    elif num1[j] == num2[j] :
        if  j>1 :
            continue
        else :
            print("".join(num1) , "=", "".join(num2))
            break
    elif num1[j] < num2[j] :
        print("".join(num1) , "<", "".join(num2))
        break
