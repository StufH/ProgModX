import pylab

data_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_y = [3, 5, 8, 13, 17, 18, 21, 23, 23, 25, 24]

def polynom1(x, a, b):
    # formel for et førstegradspolynom (en rett linje)
    return a*x + b

a1, b1, c1 = pylab.polyfit(data_x, data_y, deg=2)
# deg=1 forteller funksjonen at vi er ute etter et uttrykk med "degree" 1,
# altså et førstegradspolynom (som er en rett linje)

# Nå skal vi tegne plotte funksjonen
x = pylab.linspace(0, 10, 1000)
y1 = polynom1(x, a1, b1)

def polynom2(x, a, b, c):
    # formel for et andregradspolynom
    return a*x**2 + b*x + c

a2, b2, c2 = pylab.polyfit(data_x, data_y, deg=2)

x = pylab.linspace(0, 10, 1000)
y2 = polynom2(x, a2, b2, c2)

pylab.plot(data_x, data_y, '.', label='Datapunkter')
pylab.plot(x, y1, label='Lineær')
pylab.plot(x, y2, label='Andregrad')
pylab.legend()
pylab.show()

