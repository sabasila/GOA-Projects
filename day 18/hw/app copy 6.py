name = input("შეიტანეთ თქვენი სახელი: ")
lastname = input("შეიტანეთ თქვენი გვარი: ")
user = [name, lastname]
sia = []

for word in user:
    user.append(word.capitalize())

i = sia[0][0] + "." + sia[1][0]
print(i)
