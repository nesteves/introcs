__author__ = 'nunoe'


def minimum_payment(start_balance, annual_rate, year_limit):

    current_guess = 0
    end_balance = start_balance

    lower_bound = float(start_balance) / (12 * year_limit)
    upper_bound = float(start_balance) * (1 + annual_rate / 12) ** (12 * year_limit) / (12 * year_limit)

    current_guess = lower_bound + (upper_bound - lower_bound) / 2
    current_result = calc_outstanding_debt(current_guess, start_balance, annual_rate, year_limit)

    while abs(current_result) > 0.01:
        if current_result < 0:
            upper_bound = current_guess
        else:
            lower_bound = current_guess

        current_guess = lower_bound + (upper_bound - lower_bound) / 2
        current_result = calc_outstanding_debt(current_guess, start_balance, annual_rate, year_limit)

    return round(current_guess, 2)


def calc_outstanding_debt(monthly_payment, start_balance, annual_rate, year_limit):
    end_balance = float(start_balance)
    for i in range(12 * year_limit):
        end_balance -= monthly_payment
        end_balance *= (1 + annual_rate / 12)
    return end_balance


if __name__ == '__main__':
    loan_value = float(999999)
    rate = 0.18
    year_limit = 1

    print 'Loan: ' + str(loan_value)
    print 'Interest rate: ' + str(rate)
    print 'Year limit: ' + str(year_limit)
    print 'Lowest payment: ' + str(minimum_payment(loan_value, rate, year_limit))