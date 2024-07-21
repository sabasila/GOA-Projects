words = []
for i in range(5):
    word = input("შეიტანეთ სიტყვა ")
    words.append(word)
c = input("შეიტანეთ შესაერთებელი :  ")
result = ""
for i in range(len(words)):
    if i % 2 == 0:
        result += words[i] + c
    else:
        result += words[i]
print(result)
