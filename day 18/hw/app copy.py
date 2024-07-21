counter = 0
while True:
    word = input("შეიტანეთ სიტყვა: ")
    counter += 1
    f = False
    for letter in word:
        if letter.islower():
            f = True
            break
    if f:
        print("სიტყვაში არის lowercase ასოები")
    else:
        break
print(f"სიტყვა შეტანილი იყო {counter} ჯერ.")
