def list_sum(list1):
    total = 0
    for element in list1:
        if isinstance(element, list):
            total += list_sum(element)
        else:
            total += element
    return total
list1 = [1, [2, [3, 4], 5], 6]
print(list_sum(list1))
