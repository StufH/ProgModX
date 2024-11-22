from pylab import *

liste_aar = []
liste_utbredelse = []

# Åpne fil
fil = open("1_antarktis.txt", "r")
fil.readline()
fil.readline()

# Lese av fil
for rad in fil:
    data = rad.split(";")
    liste_aar.append(int(data[0]))
    liste_utbredelse.append(float(data[1]))
fil.close()


# lage polynom funksjoner
def polynom1(x, a, b):
    return (a * x) + b  # ax + b


def polynom2(x, a, b, c):
    return (a * x ** 2) + (b * x) + c  # ax^2 + bx + c


def polynom3(x, a, b, c, d):
    return (a * x ** 3) + (b * x ** 2) + (c * x) + d  # ax^3 + bx^2 + cx + d


# Finne koeffisientene til funksjonene
a1, b1 = polyfit(liste_aar, liste_utbredelse, deg=1)
a2, b2, c2 = polyfit(liste_aar, liste_utbredelse, deg=2)
a3, b3, c3, d3 = polyfit(liste_aar, liste_utbredelse, deg=3)

# Finne svarene på funksjonene
x = linspace(liste_aar[0], 2050, 1000)
y1 = polynom1(x, a1, b1)
y2 = polynom2(x, a2, b2, c2)
y3 = polynom3(x, a3, b3, c3, d3)

# Halveringsmetoden
noyaktighet = 1E-10

def f(x):
    return polynom2(x, a2, b2, c2)

a = liste_aar[0]
b = 2050
c = (a + b) / 2

while abs(f(c)) >= noyaktighet:
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c
    c = (a + b) / 2


print(f"{round(a2, 2)}x^2 + {round(b2, 2)}x + {round(c2, 2)}")

# Plotting
plot(liste_aar, liste_utbredelse, ".")
plot(x, y1)
plot(x, y2)
plot(x, y3)
plot(c, 0, "o")
title("Utvikling av is på sørpolen")
xlabel("År")
ylabel("Utbredelse (km2)")
legend(["datapunkter", "Lineær", "Andregrads", "Tredjegrads", "Tomt for is (år 2037.6)"])
grid()
axhline(y=0, color="black")  # Her lager jeg to linjer i x = 0 og y = 0
print(f"Det vil være tomt for is i antarktis i år {round(c, 2)}")
show()



#
# def f(x):
#     return polynom1(x, a1, b1)
#
#
# a = liste_aar[0]
# b = 3000
# c1 = (a + b) / 2
#
# while abs(f(c1)) >= noyaktighet:
#     if f(a) * f(c1) < 0:
#         b = c1
#     else:
#         a = c1
#     c1 = (a + b) / 2
# print(f"Det vil være tomt for is i antarktis i år {round(c1, 2)}")
