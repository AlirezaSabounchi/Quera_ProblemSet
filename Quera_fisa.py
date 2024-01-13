num1 = input()
num2 = input()
num3 = input()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if num1**2 + num2**2 != num3**2 and num1**2 + num3**2 != num2**2 and num2**2 + num3**2 != num1**2 :
    print("NO")

else : print ("YES")
