"""
Raise to power
"""
def pwr(x,y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x*(pwr(x,y-1)) 
def main():
    print("This program calculates exponential values.")
    a = int(input("Enter the base: "))
    b = int(input("Enter the power: "))
    print(str(a) + "^" + str(b) + " = " + str(pwr(a,b)))
main()