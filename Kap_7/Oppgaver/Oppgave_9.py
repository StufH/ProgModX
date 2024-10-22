#a
from pylab import *
h = 1E-10
t = linspace(0, 60, 1000)

def T(t): #T(t) = celcius
    return 70*(e**(-0.065*t)) #t = minutter

def derivert(T, t):
    der = ((T(t + h)) - T(t)) / h
    return der

plot(t, derivert(T, t))

#b
plot(t, T(t))
legend(["Derivet", "T(t)"])
grid()
show()

#c
print(derivert(T, t[42]))