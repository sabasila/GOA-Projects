my_info = {
    "name": "John",
    "age": 30,
    "relation": "self"
}

friend_info = {
    "name": "Alice",
    "age": 28,
    "relation": "friend"
}

family_member1_info = {
    "name": "Bob",
    "age": 55,
    "relation": "father"
}

family_member2_info = {
    "name": "Mary",
    "age": 50,
    "relation": "mother"
}

my = []
friend = []
family1 = []
family2 = []

for value in my_info.values():
    my.append(value)

for value in friend_info.values():
    friend.append(value)

for value in family_member1_info.values():
    family1.append(value)

for value in family_member2_info.values():
    family2.append(value)

c = my + friend + family1 + family2

print(c)
