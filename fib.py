"""
Fibonacci
"""
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

def main():
    print("This program calculates numbers in the Fibonacci sequence.")
    fibNum = int(input("Which place in the sequence do you want to calculate? "))
    print("Fibonacci(" + str(fibNum) + ") is", fib(fibNum))
main()