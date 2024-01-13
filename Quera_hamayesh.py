input = input()
input = input.split()
row = 11 - int(input[0])
if int(input[1]) <= 10 :
    dir = "Right"
    col = int(input[1])
else :
    dir = "Left"
    col = 21 - int(input[1])
print(dir, row, col)
