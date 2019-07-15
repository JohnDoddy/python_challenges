# implenting binary search
# by John Doddy

# data set
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# number we are looking for
target_value = int(input("What's the number you want to check"))

# function implementation
def binary_search(prime, target_value):
    minimum = 0
    maximum = len(prime) - 1
    average = (minimum + maximum) / 2 
    guess = None
    while minimum < maximum:
        if prime[average] == target_value:
            return average
        elif prime[average] < target_value:
            return average + 1 + binary_search(prime[average + 1], target_value)
        else: 
            return 
