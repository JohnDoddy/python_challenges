# Given an array of integers, print elements in reverse
# order as a single line of space-separated numbers.


arr = [1, 4, 3, 2, 5, 6]

print(" ".join(str(i) for i in arr[::-1]))