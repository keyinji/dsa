new_list = [1, 2, 10]
result = new_list[0]

new_list.append(5)
print(new_list)

new_list.insert(2, 213)
print(new_list)

new_list.extend([4,7,8])
print(new_list)

if 1 in new_list: print(True)

for i in new_list:
    if i == 1:
        print(True)
