# this should take in inputs then caluclate your monthly payments
# by John Doddy

# collect data
loan_amount = float(input("What's your loan amount?: "))
interest_rate = float(input("What's the interest percentage? "))
number_of_years = float(input("What's the payment period in years?"))

# conversion for efficient calculation
years = number_of_years * 12
interest = interest_rate / 100 / 12

# formula for monthly payments
monthly_payments = loan_amount * (interest * (1 + interest) ** years) / ((1 + interest) ** years -1)

# output results
print("If you take a loan of {0}, with and interest rate of {1}, your monthly payments would be {2:2f}".format(loan_amount, interest_rate, monthly_payments))