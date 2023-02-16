import math

def months_to_str(n):
    y = n // 12
    m = n % 12
    res = 'It will take '
    if y > 0:
        res += f'{y} year{"s" if y > 1 else ""}'
    res += ' and ' if m > 0 else ''
    res += f'{m} month{"s" if m > 1 else ""}'
    res += ' to repay this loan!'
    return res

def main():
    print('What do you want to calculate?')
    print('type "n" - for number of monthly payments,')
    print('type "a" - for annuity monthly payment amount,')
    print('type "p" - for the monthly payment:')
    cmd = input()
    if cmd == 'n':
        print('Enter the loan principal:')
        loan_principal = float(input())
        print('Enter the monthly payment:')
        payment = float(input())
        print('Enter the loan interest:')
        loan_interest = float(input())
        i = loan_interest / (12 * 100)
        months_to_repay = math.ceil(math.log(payment / (payment - i * loan_principal), i + 1))
        print(months_to_str(months_to_repay))
    elif cmd == 'a':
        print('Enter the loan principal:')
        loan_principal = float(input())
        print('Enter the number of periods:')
        months = int(input())
        print('Enter the loan interest:')
        loan_interest = float(input())
        i = loan_interest / (12 * 100)
        payment = math.ceil(loan_principal * i * math.pow(1 + i, months) / (math.pow(1 + i, months) - 1))
        # last_payment = loan_principal - (months - 1) * payment
        print(f'Your monthly payment = {payment}!')
    else:
        print('Enter the annuity payment:')
        annuity_payment = float(input())
        print('Enter the number of periods:')
        months = int(input())
        print('Enter the loan interest:')
        loan_interest = float(input())
        i = loan_interest / (12 * 100)
        loan_principal = math.floor(annuity_payment / (i * math.pow(1 + i, months) / (math.pow(1 + i, months) - 1)))
        print(f'Your loan principal = {loan_principal}!')


if __name__ == '__main__':
    main()
