import scipy.special
from sympy import *
a = sympify(input("skriv inn verdien din for a (feks: 2*x, x**2, osv...): "))
b = sympify(input("skriv inn verdien din for b (feks: 2*x, x**2, osv...): "))
n = int(input("skriv inn din verdi for n (altså: (a+b)**n): "))
r = 0
L = []

while r <= n:
    L.append((scipy.special.binom(n, r))*(a**(n-r))*(b**r))
    r += 1

print(sum(L))