from pylab import *

def N(t):
    return 0.2 * e**t + 90

t = arange(0, 10)
plot(t, N(t))

grid()
show()