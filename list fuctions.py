my_list = ["a", "b", "c", "d", "e"]

my_list.remove("c")
print(my_list)

my_list.append("g")
print(my_list)

print(len(my_list))

popped_element = my_list.pop()
print(popped_element)
print(my_list)

my_list.insert("b", "c")
print(my_list)

my_list.clear()
print(my_list)

print(type(my_list))
