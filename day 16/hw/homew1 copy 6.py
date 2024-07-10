list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [9, 10, 11, 12]
list4 = [13, 14, 15, 16]

odd_numbers = []
even_numbers = []

for num in list1:
    if num % 2 != 0:
        odd_numbers.append(num)
    else:
        even_numbers.append(num)

for num in list2:
    if num % 2 != 0:
        odd_numbers.append(num)
    else:
        even_numbers.append(num)

for num in list3:
    if num % 2 != 0:
        odd_numbers.append(num)
    else:
        even_numbers.append(num)

for num in list4:
    if num % 2 != 0:
        odd_numbers.append(num)
    else:
        even_numbers.append(num)

print(odd_numbers)
print(even_numbers)
