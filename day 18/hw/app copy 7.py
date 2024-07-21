word = input("შეიტანეთ სიტყვა: ")
letter = input("შეიტანეთ საძიებელი ასო: ")
index = -1
for i, char in enumerate(word):
    if char == letter:
        index = i
        break
print(index)

