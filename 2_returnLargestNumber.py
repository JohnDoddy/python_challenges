# This should return the largest number in a given list
# By John Doddy

numbers = [1, 2, 3, 5, 67, 45, 23, 34, 55, 89, 4]

#
# The Algorithm Implementation
# 

def largest(numbers):
    max = 0
    for i in numbers:
        if i > max:
            max = i
    print(max)

largest(numbers)
    
# 
# OR in one line using in-built python function
# 

print(max(numbers))

