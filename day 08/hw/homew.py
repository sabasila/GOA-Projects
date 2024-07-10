#3

# chavwerot pirdapir funqciistvis 
def operaciebi():
    nums = [] #gavaketot sia carieli
    for i in range(5):
        num = int(input("shemoitane ricxvi"))
        nums.append(num)

    jami = sum(nums)
    gamokleba = nums[0] - nums[1] - nums[2] - nums[3] 
    gamravleba = nums[0] * nums[1] 
    gayofa = nums[0] / nums[3] 
    nashti = nums[0] % nums[1] % nums[4] 
    gayofa2 = nums[0] // nums[3] 

#4

# chavwerot pirdapir funqciistvis 
def asaki():
    age = int(input("shemoitane wlovaneba "))

    if age > 18 and age < 20:
        print(" aris 19-20 wlamde")
    else:
        print("ar aris.")

#5

print(7 > 5) 
print(74 > 5) 
print(76 > 5) 
print(77 > 5) 
print(8 > 5) 
print(5 < 219)  
print(5 < 119)
print(5 < 219)
print(5 < 139)
print(5 < 192)
print(10 <= 116)  
print(10 <= 10) 
print(10 <= 11) 
print(10 <= 10) 
print(10 <= 154) 
print(55 >= 5)
print(52 != 4)  
print(54 != 4) 
print(52 != 4) 
print(55!= 4) 
print(6 == 6) 
print(5 == 5) 
print(7 == 7) 
print(5 == 5) 
print(9 == 9) 

#6

def type():
    mteli = int(input("shemoitane mteli ricxvi "))
    floati = float(input("shemoitane atwiladi "))

    print(type(mteli))
    print(type(floati))


#7


def types():
    inti = 10
    floati = 10.5
    stri = "leqso"
  
    print(type(inti))
    print(type(floati))
    print(type(stri))



