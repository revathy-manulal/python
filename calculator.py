from math import *

def main():
    num1 = raw_input ("Enter the first number ")
    num1 = int(num1)
    if type(num1) is not int:
        print "sorry, you entered an invalid number", num1, type(num1)
        return
    op = raw_input ("Enter the operation ")
    if op == "sin":
        print sin(num1)
        return
    elif op == "cos":
        print cos(num1)
        return
    elif op == "tan":
        print tan(num1)
        return
    elif op == "sqrt":
        print sqrt(num1)
        return
    else:
        num2 = raw_input("Enter the second number ")
        num2 = int(num2)
        if type(num2) != int:
            print "sorry, you entered an invalid number"
            return
    if op == "+":
        print num1 + num2
    elif op == "-":
        print num1 - num2
    elif op == "*":
        print num1 * num2
    elif op == "/":
        print num1/num2
    elif op == "^":
        print num1 ** num2
    elif op == "%":
        print num1 % num2
    else:
        print "You have entered an invalid operation"

if __name__== "__main__":
  main()
