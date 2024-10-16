from pylab import *
x = arange(1, 2, 0.0001)
delta_x = 1E-12

def f(x):
    return x*exp(x)

def newton(f):
    der = (f(x + delta_x) - f(x - delta_x)) / (2*delta_x)
    return der

plot(x, newton(f))
plot(x, f(x))
legend(["Newtons kvotient", "Analytisk"])
show()