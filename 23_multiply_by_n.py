# hackerrank challenge
# Given an integer n, print its first 10 multiples.
# Each multiple should be printed on a new line in the form: n x i = result.


def the_math(n):
        for i in range(1, 11):
            print("{0} x {1} = {2}".format(n, i, n * i))


if __name__ == '__main__':
    n = int(input())
    the_math(n)
