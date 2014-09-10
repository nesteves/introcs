__author__ = 'nunoe'

currentBalance = float(balance)
totalPaid = float(0.0)

for i in range(1, 13):
    minimumMonthlyPayment = round(monthlyPaymentRate * currentBalance, 2)
    currentBalance -= minimumMonthlyPayment
    currentBalance = round((1 + annualInterestRate / 12) * currentBalance, 2)
    totalPaid += minimumMonthlyPayment
    print 'Month: ' + str(i)
    print 'Minimum monthly payment: ' + str(minimumMonthlyPayment)
    print 'Remaining balance: ' + str(currentBalance)

print 'Total paid: ' + str(totalPaid)
print 'Remaining balance: ' + str(currentBalance)