import sys
from collections import namedtuple

Tax1 = namedtuple('Tax1',['income_line','income_rate','income_quick'])

Tax1 =[Tax1(80000,0.45,15160),
       Tax1(55000,0.35,7160),
       Tax1(35000,0.3,4410),
       Tax1(25000,0.25,2660),
       Tax1(12000,0.2,1410),
       Tax1(3000,0.1,210),
       Tax1(0,0.03,0)]

Tax2={'YL':0.08,'YiL':0.02,'SHY':0.005,'GS':0.00,'SY':0.00,'GJJ':0.06}

Tax3 = 5000

def cal1(income):
    wx = income * sum(Tax2.values())
    real_income = income -wx
    tax_income = real_income - Tax3
    for i in Tax1:
        if tax_income >i.income_line:
            tax = tax_income*i.income_rate-i.income_quick
            return '{:.2f}'.format(real_income-tax)
        
    return '{:.2f}'.format(real_income)

def main():
    for i in sys.argv[1:]:
        employee_id,income = i.split(':')
        try:
            income1=int(income)
        except ValueError:
            print("Parameter Error")
        income2 = cal1(income1)
        print('{}:{}'.format(employee_id,income2))
if __name__ == '__main__':
    main()
            

