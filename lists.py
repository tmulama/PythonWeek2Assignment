my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

my_list2 = [50, 60, 70]

my_list.extend(my_list2)

del my_list[-1]

my_list.sort

index = my_list.index(30)

print(index)

print(my_list)
