# hackerrank challenge
# add a meal bill which takes the parameters meal_cost,
# tip_percent and tax-percent
def solve(meal_cost, tip_percent, tax_percent):
    tip = (tip_percent / 100) * meal_cost
    tax = (tax_percent / 100) * meal_cost
    print(round(tip + tax + meal_cost))


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)