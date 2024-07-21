# სიაში ამატების მეთოდი - append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # უნდა დაბრუნდეს [1, 2, 3, 4]

# სიაში წაშლის მეთოდი - pop
popped_value = my_list.pop()
print(popped_value)  # უნდა დაბრუნდეს 4
print(my_list)  # უნდა დაბრუნდეს [1, 2, 3]

# სიაში ელემენტის ჩასმის მეთოდი - insert
my_list.insert(0, 0)
print(my_list)  # უნდა დაბრუნდეს [0, 1, 2, 3]

# სიის სიგრძე - len
print(len(my_list))  # უნდა დაბრუნდეს 4
