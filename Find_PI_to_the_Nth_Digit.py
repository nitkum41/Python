
import math, sys
from decimal import *
getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)

def factorial(n):
	"""
	Return the Factorial of a number using recursion
	Parameters:
	n -- Number to get factorial of
	"""
	if not n:
		return 1
	return n*factorial(n-1)

def getIteratedValue(k):
	"""
	Return the Iterations as given in the Chudnovsky Algorithm.
	k iterations gives k-1 decimal places.. Since we need k decimal places
	make iterations equal to k+1

	Parameters:
	k  -- Number of Decimal Digits to get
	"""
	k = k+1
	getcontext().prec = k  #round off to k values after decimal
	sum=0
	for k in range(k):
		first = factorial(6*k)*(13591409+545140134*k)
		down = factorial(3*k)*(factorial(k))**3*(640320**(3*k))
		sum += first/down
	return Decimal(sum)


def getValueOfPi(k):
	"""
	Returns the calculated value of Pi using the iterated value of the loop
	and some division as given in the Chudnovsky Algorithm
	Parameters:
	k -- Number of Decimal Digits upto which the value of Pi should be calculated
	"""
	iter = getIteratedValue(k)
	up = 426880*math.sqrt(10005)
	pi = Decimal(up)/iter

	return pi


def main():
    print ("Welcome to Pi Calculator.  Enter the number of digits upto which the value of Pi should be calculated or enter quit to exit")
    while True:
        entry = input()
        if entry == "quit":
                break
        if not entry.isdigit():
                print ("You did not enter a number. Try again")
        else:
                print (getValueOfPi(int(entry)))


if __name__=='__main__':
    main()
