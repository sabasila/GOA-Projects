def filt(numbers):
    p = []
    n= []
    
    for number in numbers:
        if number >= 0:
            p.append(number)
        else:
            n.append(number)
    
    return p, n

numbers = [1, -2, 3, -4, 5]
positive, negative = filt(numbers)

print(positive)
print(negative)
