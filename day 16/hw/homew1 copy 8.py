list1 = [1, 'a', 2, 'b']
list2 = [3, 'c', 4, 'd']
list3 = ['e', 5, 'f', 6]
all_integers = []
all_strings = ""
for lst in [list1, list2, list3]:
    for item in lst:
        if isinstance(item, int):
            all_integers.append(item)
        elif isinstance(item, str):
            all_strings += item
print(all_integers)
print(all_strings)
