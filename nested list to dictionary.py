def list_to_dict(list1, frequency=None):
    if frequency is None:
        frequency = {}
    for element in lst:
        if isinstance(element, list):
            nested_list_to_dict(element, freq)
        else:
            frequency[element] = frequency.get(element, 0) + 1
    return frequency
list1 = [1, [2, [3, 2, 4], 5, 1], 6]
print(list_to_dict(list1,None))
