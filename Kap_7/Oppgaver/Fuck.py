from pylab import *

def f(x):
    return x*2+1

def derivere(x, delta_x):
    fder = (f(x + delta_x) - f(x-delta_x)) / 2*delta_x
    return fder

print(derivere(1, 1E-8))


def integrere(a,b,n):
    h = (b-a)/n
    total = (f(a) + f(b)) / 2
    for k in range(1, n):
        total += f(a + (k*h))
    return h*total

print(integrere(0,5,1000))