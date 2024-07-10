num1 = float(input("pirveli ricxvi "))
num2 = float(input("meore ricxvi "))
operation = input(" (+, -, *, /): ")

if operation == "+":
        print(str(num1 + num2))
elif operation == "-":
        print(str(num1 - num2))
elif operation == "*":
        print(str(num1 * num2))
elif operation == "/":
        if num2 != 0:
            print(str(num1 / num2))
        else:
            print("ver gayof 0 ze ")
else:
        print("araswori simboloa ")
