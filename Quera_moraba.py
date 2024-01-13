inp = input()
inp = int(inp)
for i in range(inp) :
    if i == 0 or i == inp-1 :
        [print("*" , end = '') for j in range(inp)]
        print()
    else :
        print("*" , "*".rjust(inp-2))
