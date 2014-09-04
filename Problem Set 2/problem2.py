''' CORRECT biiiiitccch!
balance: the outstanding balance on the credit card
annualInterestRate: annual interest rate as a decimal
monthlyPaymentRate: minimum monthly payment rate as a decimal

monthly interest rate: annualInterestRate/12.0
#minimum monthly payment: monthlyPaymentRate*balance(n-1)
monthly unpaid balance: balance(n-1)-minMonthlyPayment
updated balance each month: monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)

'''

#Remove these, it's for testing
balance = 3329
annualInterestRate = 0.2

#Copy this --->
monthlyInterestRate = annualInterestRate / 12.0
minimumMonthlyPayment = 0

def calculateAnnualBalance(minimumMonthlyPayment):
    balances = [balance]
    for iteration in range(1, 13):          
        prev_balance = balances[iteration-1]
        
        unpaidBalance = prev_balance - minimumMonthlyPayment
        updatedBalance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        balances.append(updatedBalance)

        if iteration == 12:
            return updatedBalance
    

while calculateAnnualBalance(minimumMonthlyPayment) > 0:
    minimumMonthlyPayment += 10
    calculateAnnualBalance(minimumMonthlyPayment)

print "Lowest payment: " + str(round(minimumMonthlyPayment, 2))