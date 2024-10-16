from pylab import *
import sympy as sp
x = sp.symbols("x")

def f(x):
    return 4 * 5**((x**3) - (2*x))

def Newton(f, x, h):
    fder = (f(x+h) - f(x))/(h)
    return fder

h = [10**-i for i in range(1, 1000)]

if __name__ == "__main__":

    fil = open("Newtons_kvotient.txt", "a")
    fil.write(f"{(f(x))}:\n")
    x = [2, 3, 4, 5]
    for i in range(len(x)):
        fil.write(f"For h = {h[i]} : {Newton(f, x[i], h[i])}\n")

    fil.close()