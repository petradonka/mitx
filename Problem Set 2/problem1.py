''' CORRECT
balance: the outstanding balance on the credit card
annualInterestRate: annual interest rate as a decimal
monthlyPaymentRate: minimum monthly payment rate as a decimal

monthly interest rate: annualInterestRate/12.0
minimum monthly payment: monthlyPaymentRate*balance(n-1)
monthly unpaid balance: balance(n-1)-minMonthlyPayment
updated balance each month: monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

'''

#Remove these, it's for testing
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#Copy this --->
monthlyInterestRate = annualInterestRate / 12.0
balances = [balance]
payments = [0]

for iteration in range(1, 13):
    prev_balance = balances[iteration-1]
    
    print "Month: " + str(iteration)
    
    minimumMonthlyPayment = monthlyPaymentRate * prev_balance
    payments.append(minimumMonthlyPayment)
    print "Minimum monthly payment: " + str(round(minimumMonthlyPayment, 2))
    
    unpaidBalance = prev_balance - minimumMonthlyPayment
    updatedBalance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    balances.append(updatedBalance)
    print "Remaining balance: " + str(round(updatedBalance, 2))
    
print "Total paid: " + str(round(sum(payments), 2))
print "Remaining balance: " + str(round(balances[-1], 2))