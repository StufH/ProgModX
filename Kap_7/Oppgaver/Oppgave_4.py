from pylab import *
t = arange(0,11)
h = 1E-5

def x(t):
    return t**3 + 1/3 * t

def hastighet(t):
    der = (x(t + h) - x(t - h)) / (2*h)
    return der

def akselerasjon(t):
    der = (hastighet(t + h) - hastighet(t - h)) / (2*h)
    return der

#x(t) = posisjon
#x'(t) = hastighet
#x''(t) = akselerasjon



plot(t, x(t))
plot(t, hastighet(t))
plot(t, akselerasjon(t))
legend(["posisjon", "hastighet", "akselerasjon"])
show()
