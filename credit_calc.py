import math
import argparse

def flag_p():
    credit_inter = args.interest / 1200
    periods = args.periods
    monthly_pay = args.payment
    credit_princ = monthly_pay / ((credit_inter * (1 + credit_inter)**periods) / ((1 + credit_inter)**periods - 1))
    print("Your annuity payment = ", int(credit_princ // 1), "!", sep = "")
    print("Overpayment =", math.ceil(monthly_pay * periods - credit_princ))


def flag_a():
    credit_inter = args.interest / 1200
    periods = args.periods
    credit_princ = args.principal
    monthly_pay = credit_princ * (credit_inter * (1 + credit_inter)**periods) / ((1 + credit_inter)**periods - 1)
    print("Your annuity payment = ", int(math.ceil(monthly_pay)), "!", sep = "")
    print("Overpayment =", int(math.ceil(monthly_pay)) * periods - credit_princ)

def flag_n():
    credit_inter = args.interest / 1200
    credit_princ = args.principal
    monthly_pay = args.payment
    periods = math.log((monthly_pay / (monthly_pay - credit_inter * credit_princ)), (1 + credit_inter))
    if round(periods, 0) >= 12:
        year = round(periods, 0) // 12
        month = math.ceil(periods) % 12
        if month == 0:
            print("You need ", int(year), " years to repay this credit!", sep = "")
        else:
            print("You need ", int(year), " years and ", month, " months to repay this credit!", sep = "")
    else:
        print("You need ", periods, " months to repay this credit!", sep = "")
    print("Overpayment =", int(monthly_pay * round(periods, 0) - credit_princ))

def validation(args):
    i = 0
    for x, y in args.__dict__.items():
        if y == None:
            i += 1
    if i >= 2:
        print("Incorrect parameters.")
    elif args.type != "diff" and args.type != "annuity":
        print("Incorrect parameters.")
    elif args.type == "diff" and args.payment:
        print("Incorrect parameters.")
    elif (args.payment and args.payment < 0) or (args.principal and args.principal < 0) or (args.periods and args.periods < 0) or (args.interest and args.interest < 0):
        print("Incorrect parameters.")
    elif args.principal and args.payment and args.periods:
        print("Incorrect parameters.")
    else:
        return 0
    return 1

def flag_d():
    credit_princ = args.principal
    credit_inter = args.interest / 1200
    periods = args.periods
    overpayment = 0
    for i in range (1, periods + 1):
        monthly_pay = credit_princ / periods + credit_inter * (credit_princ - (credit_princ * (i - 1)) / (periods))
        print("Month ", i, ": paid out ", int(math.ceil(monthly_pay)), sep = "")
        overpayment += int(math.ceil(monthly_pay))
    print("\nOverpayment =", overpayment - credit_princ)

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, help= "type: diff or annuity")
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type= int)
parser.add_argument("--interest", type= float)
args = parser.parse_args()    
if validation(args) == 0:
    if args.type == "diff":
        if args.principal and args.interest and args.periods:
            flag_d()
    elif args.type == "annuity":
        if args.payment and args.principal and args.interest:
            flag_n()
        elif args.principal and args.interest and args.periods:
            flag_a()
        elif args.payment and args.interest and args.periods:
            flag_p()
