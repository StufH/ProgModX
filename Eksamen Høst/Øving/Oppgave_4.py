from pylab import *

liste_aar = []
liste_populasjon = []

fil = open("4_populasjon.txt", "r")
fil.readline()
fil.readline()

for linje in fil:
    data = linje.split(";")
    liste_aar.append(float(data[0]))
    liste_populasjon.append(float(data[1]))
fil.close()


def polynom1(x, a, b):
    return (a * x) + b


def polynom2(x, a, b, c):
    return (a * x ** 2) + (b * x) + c


def polynom3(x, a, b, c, d):
    return (a * x ** 3) + (b * x ** 2) + (c * x) + d


a1, b1 = polyfit(liste_aar, liste_populasjon, deg=1)
a2, b2, c2 = polyfit(liste_aar, liste_populasjon, deg=2)
a3, b3, c3, d3 = polyfit(liste_aar, liste_populasjon, deg=3)

x = linspace(liste_aar[len(liste_aar) - 1], 2050, 1000)
y1 = polynom1(x, a1, b1)
y2 = polynom2(x, a2, b2, c2)
y3 = polynom3(x, a3, b3, c3, d3)

y3_2030 = polynom3(2030, a3, b3, c3, d3)

plot(liste_aar, liste_populasjon, ".")
plot(x, y1)
plot(x, y2)
plot(x, y3)
xlabel("år")
ylabel("populasjon i tiende milliard")
xlim(liste_aar[len(liste_aar) - 1], 2050)
legend(["datapunkter", "Lineær", "Andregrads", "Tredjegrads"])
show()

print(f"det er {y3_2030 * 1E-9:.2f} milliarder personer i 2030")
