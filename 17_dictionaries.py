# a dictionary/ hashtable
values = {"name":"John", "age": 19}

# traversing a dictionary
for key, value in values.items():
    print("My {} is {}".format(key, value))

# updating dictionary values
values["name"] = "Doddy"
print(values["name"])

# deleting dictionary items
values.__delitem__("name")
print(values)