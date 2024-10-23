import numpy as np
Posisjon = []
Tid = []

fil = open("Oppgave_12t.txt", "r")
fil.readline()
for line in fil:
    x, y = map(float, line.split(","))

    Posisjon.append(y)
    Tid.append(x)

Posisjon = np.array(Posisjon)
Tid = np.array(Tid)

