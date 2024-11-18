from pylab import *

N = 100
t = linspace(0,10,N)
v0 = 0
a = 0.14
s = v0*t + 0.5*a*t**2
fil = open("bevegelse.txt", "w")
fil.write("Tid Akselerasjon \n")

for i in range(N):
    fil.write(str(t[i]))
    fil.write("    ")
    fil.write(str(s[i]) + "\n")
fil.close()