import argparse
import math


def months_to_str(n):
    y = n // 12
    m = n % 12
    res = 'It will take '
    if y > 0:
        res += f'{y} year{"s" if y > 1 else ""}'
    res += ' and ' if m > 0 and y > 0 else ''
    if m > 0:
        res += f'{m} month{"s" if m > 1 else ""}'
    res += ' to repay this loan!'
    return res


def calculate_annuity_n(args):
    i = args['interest'] / (12 * 100)
    months_to_repay = math.ceil(math.log(args['payment'] / (args['payment'] - i * args['principal']), i + 1))
    print(months_to_str(months_to_repay))
    print(f"Overpayment = {args['payment'] * months_to_repay - args['principal']}")


def calculate_annuity_a(args):
    i = args['interest'] / (12 * 100)
    payment = math.ceil(args['principal'] * i * math.pow(1 + i, args['periods']) / (math.pow(1 + i, args['periods']) - 1))
    print(f"Your annuity payment = {payment}!")
    print(f"Overpayment = {payment * args['periods'] - args['principal']}")


def calculate_annuity_p(args):
    i = args['interest'] / (12 * 100)
    loan_principal = math.floor(args['payment'] / (i * math.pow(1 + i, args['periods']) / (math.pow(1 + i, args['periods']) - 1)))
    print(f'Your loan principal = {loan_principal}!')


def calculate_diff(args):
    s = 0
    i = args['interest'] / (12 * 100)
    for m in range(1, args['periods'] + 1):
        dm = math.ceil(args['principal'] / args['periods'] + i * args['principal'] * (1 - (m - 1) / args['periods']))
        s += dm
        print(f"Month {m}: payment is {dm}")
    print(f"Overpayment = {s - args['principal']}")


def main():
    invalid_params_msg = 'Incorrect parameters'
    parser = argparse.ArgumentParser()
    parser.add_argument("--principal", type=int, default=0)
    parser.add_argument("--payment", type=int, default=0)
    parser.add_argument("--periods", type=int, default=0)
    parser.add_argument("--interest", type=float, default=0)
    parser.add_argument("--type", type=str, default='')
    args = vars(parser.parse_args())
    if (args.get('type') == 'annuity'
            and args.get('principal') > 0
            and args.get('payment') > 0
            and args.get('interest') > 0):
        calculate_annuity_n(args)
    elif (args.get('type') == 'annuity'
            and args.get('principal') > 0
            and args.get('periods') > 0
            and args.get('interest') > 0):
        calculate_annuity_a(args)
    elif (args.get('type') == 'annuity'
            and args.get('payment') > 0
            and args.get('periods') > 0
            and args.get('interest') > 0):
        calculate_annuity_p(args)
    elif (args.get('type') == 'diff'
            and args.get('principal') > 0
            and args.get('periods') > 0
            and args.get('interest') > 0):
        calculate_diff(args)
    else:
        print(invalid_params_msg)


if __name__ == '__main__':
    main()
