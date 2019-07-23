# this program should return the sum of the integers in an array

# the array 
numbers = [2, 6, 7, 8, 9, 10, 21, 34]

# the implementation
def return_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

return_sum(numbers)


# or
print(sum(numbers))