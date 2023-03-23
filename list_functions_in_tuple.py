my_tuple = ['N', 'e','e','l','e','s','h']


my_list = list(my_tuple)

my_list.remove('e')
print(my_list)

my_list.append('U')
print(my_list)

print(len(my_list))

popped_element = my_list.pop()
print(popped_element)
print(my_list)

my_list.insert(2, 3)
print(my_list), 

my_list.clear()
print(my_list)

print(type(my_list))

my_tuple = tuple(my_list)
print(my_tuple)