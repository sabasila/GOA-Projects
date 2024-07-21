def sash(numbers):
    if not numbers:
        return 0  
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
print(sash(numbers))
