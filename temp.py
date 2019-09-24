from decimal import *
getcontext().prec = 50

def onepointonezero(a, b, c):
    a = Decimal(a)
    b = Decimal(b)
    c = Decimal(c)
    bsq = Decimal.sqrt(b**2 - 4 * a * c)
    x1 = (-b + bsq) / (2*a)
    x2 = (-b - bsq) / (2*a)
    return (x1, x2)

print(onepointonezero(Decimal(10**-155), Decimal(-10**155), Decimal(10**155)))