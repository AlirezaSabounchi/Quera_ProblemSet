def factorial(numb):

    fact = 1
    for i in range(1,numb+1) :
        fact = fact*i
    return fact

if __name__ == "__factorial__" : factorial()
###
while True :
    number = input()

    try :
        number = int(number)
        break
    except :
        print("Invalid input, Try Again!")
        continue

result = factorial(number)
print(result)
