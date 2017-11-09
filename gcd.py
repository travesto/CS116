"""
Euclid's GCD
"""
def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)
def main():
    print("This program calculates the greatest common divisor (GCD) for two integers.\n")
    a = int(input("Enter a number: "))
    b = int(input("Enter another: "))
    print("\nGCD =",gcd(a,b))

main()