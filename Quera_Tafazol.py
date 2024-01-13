def game(self, number) :
#    while True :
    number = input(number)
    number = int(number)
#        if number > 99 or number < 10 :
#            print("Number must be between 10 and 99")
#            continue
#        else : break

    tens = number // 10
    ones = number % 10

    if tens > ones :
        result = tens - ones
    else :
        result = ones - tens

    return result
if __name__ == "__game__" : game()
