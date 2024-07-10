def pop_operations():
    numbers = [1, 2, 3, 4, 5]
    last_element = numbers.pop()
    print("Removed element:", last_element)
    print("Updated list:", numbers)
    strings = ["apple", "banana", "cherry", "date"]
    first_element = strings.pop(0)
    print("Removed element:", first_element)
    print("Updated list:", strings)
    characters = ['a', 'b', 'c', 'd', 'e']
    element_at_index_2 = characters.pop(2)
    print("Removed element:", element_at_index_2)
    print("Updated list:", characters)

    tuples = [(1, 2), (3, 4), (5, 6)]
    last_tuple = tuples.pop()
    print("Removed tuple:", last_tuple)
    print("Updated list:", tuples)

def count_operations():
    numbers = [1, 5, 2, 5, 3, 5, 4, 5]
    count_5 = numbers.count(5)
    print("Count of number 5:", count_5)

    strings = ["apple", "banana", "orange", "grape"]
    count_a = sum(s.count('a') for s in strings)
    print("Count of letter 'a':", count_a)

    booleans = [True, False, True, False, True]
    count_true = booleans.count(True)
    print("Count of True values:", count_true)

    nested_list = [[1, 2], [3, 4], [5, 6], [3, 4]]
    count_sublist = sum(1 for sublist in nested_list if sublist == [3, 4])
    print("Count of sublist [3, 4]:", count_sublist)

def max_operations():

    numbers = [10, 5, 20, 15, 30]
    max_number = max(numbers)
    print("Maximum number:", max_number)
    strings = ["apple", "banana", "orange", "grape"]
    max_length = max(len(s) for s in strings)
    print("Maximum string length:", max_length)
    ages = [25, 30, 20, 35, 40]
    oldest_age = max(ages)
    print("Oldest person's age:", oldest_age)

def min_operations():
    numbers = [10, 5, 20, 15, 30]
    min_number = min(numbers)
    print("Smallest number:", min_number)

    strings = ["apple", "banana", "orange", "grape"]
    shortest_word = min(strings, key=len)
    print("Shortest word:", shortest_word)

    temperatures = [-5, 0, 10, -2, 3]
    lowest_temp = min(temperatures)
    print("Lowest temperature:", lowest_temp)

    products = [("apple", 2.5), ("banana", 1.8), ("orange", 3.2)]
    min_price = min(products, key=lambda x: x[1])[1]
    print("Minimum price:", min_price)

def sum_operations():
    numbers = [1, 2, 3, 4, 5]
    total_sum = sum(numbers)
    print("Total sum:", total_sum)

    strings = ["apple", "banana", "orange", "grape"]
    total_length = sum(len(s) for s in strings)
    print("Total length of strings:", total_length)

    scores = [10, 5, 15, 8, 12]
    total_score = sum(scores)
    print("Total score:", total_score)

    nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
    flattened_sum = sum(sum(sublist) for sublist in nested_lists)
    print("Flattened sum:", flattened_sum)

def len_operations():

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    num_elements = len(weekdays)
    print("Number of elements:", num_elements)

    nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
    length = sum(len(sublist) for sublist in nested_list)
    print("Length of nested list:", length)
