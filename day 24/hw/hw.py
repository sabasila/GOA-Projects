def sum_of_integers(mixed_list):
    total_sum = 0
    for item in mixed_list:
        if isinstance(item, int):
            total_sum += item
    return total_sum

def sum_of_numbers(number_list):
    return sum(number_list)

def list_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def convert_case(input_string):
    result = ""
    for char in input_string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char  
    return result


