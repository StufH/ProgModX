from pylab import *

a = -0.6554
b = 3.8662
noyaktighet = 0.0000000001


def f(x):
    return 0.5 * x ** 3 - 2 * x ** 2 + 1 # 0.5x^3 - 2x^2 + 1


m = (a + b) / 2

while abs(f(m)) >= noyaktighet:
    if f(a) * f(m) < 0:
        b = m
    else:
        a = m

    m = (a + b) / 2

print(f"Løsningen på likningen er tilnærmet lik {round(m, 4)}")