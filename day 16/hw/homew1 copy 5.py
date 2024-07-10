list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = [9, 10, 11, 12]
list4 = [13, 14, 15, 16]

sum_odd1 = sum(num for num in list1 if num % 2 != 0)
sum_even1 = sum(num for num in list1 if num % 2 == 0)
sum_odd2 = sum(num for num in list2 if num % 2 != 0)
sum_even2 = sum(num for num in list2 if num % 2 == 0)
sum_odd3 = sum(num for num in list3 if num % 2 != 0)
sum_even3 = sum(num for num in list3 if num % 2 == 0)
sum_odd4 = sum(num for num in list4 if num % 2 != 0)
sum_even4 = sum(num for num in list4 if num % 2 == 0)
print(f"Sum of odd numbers in list1: {sum_odd1}")
print(f"Sum of even numbers in list1: {sum_even1}")
print(f"Sum of odd numbers in list2: {sum_odd2}")
print(f"Sum of even numbers in list2: {sum_even2}")
print(f"Sum of odd numbers in list3: {sum_odd3}")
print(f"Sum of even numbers in list3: {sum_even3}")
print(f"Sum of odd numbers in list4: {sum_odd4}")
print(f"Sum of even numbers in list4: {sum_even4}")


