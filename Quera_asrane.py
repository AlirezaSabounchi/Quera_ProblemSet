num_loads = input()
num_loads = int(num_loads)
list_loads = input().split()
list_loads = list(map(int, list_loads))
truck_index = [1]*num_loads
sum = 0
init_list = list_loads.copy()
list_loads.sort(reverse = True)
for i in range(num_loads) :
        sum += list_loads[i]
        if sum < 20 :
            continue
        elif sum == 20 :
            sum = 0
            if i != num_loads-1 :
                for j in range(i+1 , num_loads):
                    truck_index[j] += 1
        elif sum > 20 :
            sum = list_loads[i]
            for j in range(i , num_loads):
                truck_index[j] += 1
print(max(truck_index))
init_truck = [0]*num_loads

for i in range(num_loads) :
    for j in range(num_loads) :
        if list_loads[i] == init_list[j] :
            init_truck[j] = truck_index[i]
            init_list[j] = -1
            break
res = [0]*num_loads
index = 1
for i in range(num_loads):
    temp = init_truck[i]
    if temp != 0 :
        for j in range(i , num_loads):
            if init_truck[j] == temp :
                res[j] = index
                init_truck[j] = 0
        index += 1
    else : continue

for i in range(num_loads):
    print(res[i], end = " ")
