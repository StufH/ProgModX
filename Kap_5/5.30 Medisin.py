from pylab import *
K0 = 4.73
a = 0.65
y = [] #Lager en liste for å lagre plottingene
x = [] #Lager en liste med timene

def K(t):
    return K0*(e**(-a*t))

for i in range(0, 48):
    y.append(K(i))
    x.append(i)

plot(x, y)
xlabel("timer")
ylabel("Konsentrasjon")
title("Modell for hvor mye konsentrasjon av medisinen vil være igjen")
grid()
show()

#Tror den er ferdig men vet ikke svar