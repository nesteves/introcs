__author__ = 'nunoe'


def minimum_payment(start_balance, annual_rate, year_limit):
    """" function docstring

    :param start_balance:
    :param annual_rate:
    :param year_limit:
    :return: the minimum amount to be paid for the loan monthly
    """
    current_guess = 0
    end_balance = start_balance

    while end_balance > 0:
        end_balance = float(start_balance)
        current_guess += 10

        for i in range(12 * year_limit):
            end_balance -= current_guess
            end_balance *= (1 + annual_rate / 12)

    return current_guess


if __name__ == '__main__':
    loan_value = float(3329)
    rate = 0.2
    year_limit = 1

    print 'Loan: ' + str(loan_value)
    print 'Interest rate: ' + str(rate)
    print 'Year limit: ' + str(year_limit)
    print 'Lowest payment: ' + str(minimum_payment(loan_value, rate, year_limit))