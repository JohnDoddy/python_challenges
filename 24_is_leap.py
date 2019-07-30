# hackerrank challenge
# You are given the year, and you have to write a function to check if the year is leap or not.
# In the Gregorian calendar three criteria must be taken into account to identify leap years:

# 1. The year can be evenly divided by 4, is a leap year, unless:
# 2. The year can be evenly divided by 100, it is NOT a leap year, unless:
# 3. The year is also evenly divisible by 400. Then it is a leap year.


def is_leap(year):
    leap = False

    if year % 4 == 0:
        divide_hun = year // 100
        divide_four_hun = year // 400
        if divide_hun and divide_four_hun % 2 == 0:
            leap = True
        if year == 2000:
            leap = True
        if year == 2400:
            leap = True
    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))
