numbers = [10, 5, 20, 15, 3, 8]
n = numbers[0]
for num in numbers[1:]:
    if num > n:
        n = num

print(n)

