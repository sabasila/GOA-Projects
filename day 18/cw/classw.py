car = {
    "mark": "Ferrari",
    "name": ":aferrari",
    "year": 1980 ,
    "engine": 3.5 }

person = {
    "name": ":aferrari",
    "age": 16 }

person.update({"surname": "Silagadze"})
person["email"] = "sabasila17@gmail.com"

for key, value in person.items():
    print(key, value)


sia = {}

for i in range(1, 1001):
    key = "item_" + str(i)
    sia[key] = i + 1 

for key in sia:
    print(key)



   