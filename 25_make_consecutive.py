# codesignal challenge
# make array consecutive
# if array is not consecutive, return the amount of numbers that would make it consecutive


statues = [6, 2, 3, 8]
def makeArrayConsecutive2(statues):
    lowest_number = min(statues)
    highest_number = max(statues)
    # print(lowest_number)
    # print(highest_number)
    list = [i for i in range(lowest_number, highest_number + 1) if i not in statues]
    print(list)


makeArrayConsecutive2(statues)
