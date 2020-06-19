import math, sys
from decimal import *
getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)

def factorial(n):
    if not n:
        return 1
    return n*factorial(n-1)

def eCalc(n):
    #return round(math.e,n)
    #print('%.*f' % (40, math.e))
    """
    Using Newtn series we can calculate values upto 50 places

    n=n+1
    sum=0
    getcontext().prec=n
    for n in range(n):
        sum+=1/factorial(n)

    return Decimal(sum)

    """
    #using brothers formulae we can compute upto 50 places
    n=n+1
    sum=0

    getcontext().prec=n
    for n in range(n):
        sum+=(2*n+2)/factorial(2*n+1)
    return Decimal(sum)





def main():
    print("Welcome to E calculator !!!")

    while True:
        digits=input("Enter a number between 1 and 51 or Enter quit to exit ?")
        if digits == 'quit':
            break
        elif not digits.isdigit() or int(digits)>50:
            print("Enter a valid number please !!")
        else:
            val=eCalc(int(digits))
            print(str(val)[:int(digits)+2])



if __name__=='__main__':
    main()
