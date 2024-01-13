while True :
    number = input()
    number = int(number)
    if number>10 or number<0 :
        print("Invalid input, Try Again!")
        continue
    else :
        break
print("W", end='')
for i in range(number) :
    print("o", end='')
print("w!")
