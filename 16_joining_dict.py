# joining dictionaries

dict1 = {"mary": 19, "jenny": 20, "chloe": 22}
dict2 = {"austin": 19, "justin": 22, "john": 19}
dict3 = {"singh": 21, "patel": 23, "shah": 24}
dict3 = {**dict1, **dict2, **dict3}
print(dict3)

# explanation
# here the **kwargs argument returns plain key, value items that are in the dict

# combine lists

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [list1, list2]
print(list3)