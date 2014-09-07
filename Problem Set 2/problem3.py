'''Cooo-ooreect.
balance: the outstanding balance on the credit card
annualInterestRate: annual interest rate as a decimal

monthly interest rate: annualInterestRate/12.0
#minimum monthly payment: monthlyPaymentRate*balance(n-1)
monthly unpaid balance: balance(n-1)-minMonthlyPayment
updated balance each month: monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0
'''

#Remove these, it's for testing
balance = 999999
annualInterestRate = 0.18

#Copy this --->
originalBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
low = balance/12.0
high = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
epsilon = 0.01

while abs(balance) > epsilon:
    balance = originalBalance

    monthlyPayment = (high-low) / 2 + low

    for month in range(12):
        balance -= monthlyPayment
        balance *= 1 + monthlyInterestRate

    if balance > 0:
            low = monthlyPayment
    else:
        high = monthlyPayment

print "Lowest Payment: ", round(monthlyPayment, 2)