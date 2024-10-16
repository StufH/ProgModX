from pylab import *
h = 1E-5
t = arange(0, 21)

# t = tid/minutter
def x(t):  # meter mot øst
    return (3 * (t**2)) + (4 * t)

def y(t):  # meter mot nord
    return (5 * t) + 4

def øst_derivert(t):
    der = (x(t + h) - x(t - h)) / (2 * h)
    return der

def nord_derivert(t):
    der = (y(t + h) - y(t - h)) / (2 * h)
    return der

plot(t, øst_derivert(t))
plot(t, nord_derivert(t))
title("Speed East and North")
xlabel("Minutter")
ylabel("Speed (m/s)")
legend(["Øst", "Nord"])
show()