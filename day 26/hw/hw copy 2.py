def custom_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count
example_list = [1, 2, 3, 4, 5]
print(custom_len(example_list)) 