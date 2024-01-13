temp = 1
num = []
for i in range(4) :
    num.append(int(input()))
    temp *= num[i]
print("Sum :" , "{:.6f}".format(sum(num)))
print("Average :" , "{:.6f}".format(sum(num)/4))
print("Product :" , "{:.6f}".format(temp))
print("MAX :" , "{:.6f}".format(max(num)))
print("MIN :" , "{:.6f}".format(min(num)))
