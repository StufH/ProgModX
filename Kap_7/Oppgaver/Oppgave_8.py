from pylab import *
from Oppgave_1 import f
import sympy as sp

x = sp.symbols("x")

def Newton(f, x, h):
    fder = (f(x+h) - f(x-h))/(2*h)
    return fder

h = [10**-i for i in range(1, 1000)]

fil = open("Newtons_symmetriske_kvotient.txt", "a")
fil.write(f"{str(f(x))}:\n")
x = [2, 3, 4, 5]
for i in range(len(x)):
    fil.write(f"For h = {h[i]} : {Newton(f, x[i], h[i])}\n")

fil.close()
