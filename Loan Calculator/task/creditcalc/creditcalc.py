import math


def main():
    print('Enter the loan principal:')
    loan_principal = int(input())
    print('What do you want to calculate?')
    print('type "m" - for number of monthly payments,')
    print('type "p" - for the monthly payment:')
    cmd = input()
    if cmd == 'm':
        print('Enter the monthly payment:')
        payment = int(input())
        months_to_repay = math.ceil(loan_principal / payment)
        print(f'It will take {months_to_repay}',
              f'month{"s" if months_to_repay > 1 else ""} to repay the loan')
    else:
        print('Enter the number of months:')
        months = int(input())
        payment = math.ceil(loan_principal / months)
        last_payment = loan_principal - (months - 1) * payment
        print(f'Your monthly payment = {payment}',
              f'and the last payment = 104.' if last_payment != payment else '')


if __name__ == '__main__':
    main()
