data_list = [1, 'a', 2, 'b', 3, 'c']
integer_list = []
string_list = []
for item in data_list:
    if isinstance(item, int):
        integer_list.append(item)
    elif isinstance(item, str):
        string_list.append(item)
print(string_list)
print(integer_list)
