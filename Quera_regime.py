inp = input()
yel = inp.count("Y")
red = inp.count("R")
if red >= 3 or (yel >=2 and red >=2) or red+yel == len(inp) :
    print("nakhor lite")
else :
    print("rahat baash")
