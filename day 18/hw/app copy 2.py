word = input("შეიტანეთ სიტყვა: ")
sit = ""

for i in range(len(word)):
    if i % 2 == 0:
        sit += word[i].upper()
    else:
        sit += word[i].lower()

print(sit)
