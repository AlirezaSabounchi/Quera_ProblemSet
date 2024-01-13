def get_unique(n):
    unique = []
    unique_str = set(n)
    for i in unique_str :
        unique.append(i)
    return unique

length = int(input())
names = []
temp = []
for i in range(length) :
    names.append(list(input()))
    temp.append(len(get_unique(names[i])))
print(max(temp))
