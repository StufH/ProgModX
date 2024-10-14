from pylab import *
L = []
dt = 0
dt2 = []
t = 15

def K(x): #Kostnadd
    return (-50*(x**2))-(420*x)-50

def I(x): #Inntekt
    return 84*x

def P(x): #Profitt
    return I(x)-K(x)

while dt <= t:
    L.append(P(dt))
    dt += 0.015
    dt2.append(dt)

plot(dt2, L)
xlabel("KG")
ylabel("Profit/Kr")
grid()
show()

#Noe er feil men finner ikke enda. får feil graf