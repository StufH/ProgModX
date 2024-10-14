from pylab import *
import sympy as sp
x = sp.symbols("x")

def f(x):
    return e**x

def Newton(f, x, h):
    fder = (f(x+h) - f(x))/h
    return fder

h = [10**-i for i in range(1, 1000)]

fil = open("test.txt", "a")
fil.write(f"{f(x)}:\n")
x = [2, 3, 4, 5]
for i in range(0, len(x)):
    fil.write(f"For h = {h[i]} : {Newton(f, x[i], h[i])}\n")

fil.close()