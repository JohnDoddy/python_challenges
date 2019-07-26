# implenting binary search
# by John Doddy

# our data set
data = [1, 2, 3, 4, 5, 6]
target_value = int(input("What's the target value: "))

# the binary search algorithm
def binary_search(data, target_value):
    minimum = data[0]
    maximum = len(data) - 1
    while minimum <= maximum:
        midium = int(maximum / minimum)
        
        if data[midium] == target_value:
            print("Yes {} is on our list".format(target_value))
        if target_value > data[midium]:
            minimum = midium + 1
        else:
            maximum = midium - 1
    if minimum > maximum:
        print("Your value is not on the list")
         
            
binary_search(data, target_value)

        