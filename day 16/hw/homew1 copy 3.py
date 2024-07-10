integers = [1, 2, 3, 4]
strings = ['a', 'b', 'c', 'd']
l= []
for i in range(min(len(integers), len(strings))):
    l.append(strings[i])
    l.append(integers[i])
l.extend(strings[len(integers):])
l.extend(integers[len(strings):])
print(l)
