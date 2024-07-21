def find_index(string, char):
    index = string.find(char)
    if index == -1:
        return None
    else:
        return index
    
print(find_index("hello", "e"))  
print(find_index("hello", "z"))  
