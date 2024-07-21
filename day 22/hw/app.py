def manual_pop(lst, index=None):
    new_lst = []
    for i in range(len(lst)):
        if i != index:
            new_lst.append(lst[i])
    return new_lst

def manual_count(lst, element=None):
    if element is None:
        avg = int(sum(lst) / len(lst))
        element = avg
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

def manual_min(lst=None):
    if lst is None:
        lst = list(range(1, 11))
    if not lst:
      min_value = lst[0]

    for item in lst:
        if item < min_value:
            min_value = item
    return min_value

def manual_max(lst=None):
    if lst is None:
        lst = list(range(1, 11))
    if not lst:
       max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item
    return max_value




