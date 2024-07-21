# Task 1
def multiply_numbers(collection):
    new_list = []
    for num in collection:
        if isinstance(num, int):
            new_list.append(num * 2)
        elif isinstance(num, float):
            new_list.append(num * 4)
        else:
            new_list.append(num)
    return new_list

numbers = [1, 2.5, 3, 4.0]
print(multiply_numbers(numbers))  # Output: [2, 10.0, 6, 8.0]


# Task 2
def case_convert_names(names):
    result = []
    for index, name in enumerate(names):
        if index % 2 == 0:
            result.append(name.upper())
        else:
            result.append(name.lower())
    return result

names = ["John", "Jane", "Michael", "Emily", "David"]
print(case_convert_names(names))  # Output: ['JOHN', 'jane', 'MICHAEL', 'emily', 'DAVID']


# Task 3
def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

sentence = "this is a sample sentence"
print(capitalize_first_letter(sentence))  # Output: 'This Is A Sample Sentence'


# Task 4
def manual_pop(collection, remove_index):
    if remove_index >= len(collection):
        return "Index out of range"
    
    result = []
    for index in range(len(collection)):
        if index != remove_index:
            result.append(collection[index])
    
    return result

print(manual_pop(["Luka", "lile"], 1))  # Output: ['Luka']


# Task 5
def remove_duplicates(collection):
    return list(set(collection))

numbers = [1, 2, 3, 2, 4, 3, 5]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4, 5]


# Task 6
def find_duplicates(collection):
    unique_items = set()
    duplicates = []
    for item in collection:
        if item in unique_items:
            duplicates.append(item)
        else:
            unique_items.add(item)
    return list(set(duplicates))

numbers = [1, 2, 3, 2, 4, 3, 5]
print(find_duplicates(numbers))  # Output: [2, 3]


# Task 7
def count_occurrences(collection, search_word):
    return collection.count(search_word)

words = ["apple", "banana", "apple", "orange", "apple"]
print(count_occurrences(words, "apple"))  # Output: 3


# Task 8
def remove_even_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_even_numbers(numbers))  # Output: [1, 3, 5, 7, 9]


# Task 9
def merge_lists(list1, list2):
    return list(set(list1 + list2))

list1 = [1, 2, 3]
list2 = [3, 4, 5]
print(merge_lists(list1, list2))  # Output: [1, 2, 3, 4, 5]


# Task 10
def find_unique_elements(collection):
    unique_elements = []
    for item in collection:
        if collection.count(item) == 1:
            unique_elements.append(item)
    return unique_elements

numbers = [1, 2, 2, 3, 4, 4, 5]
print(find_unique_elements(numbers))  # Output: [1, 3, 5]
