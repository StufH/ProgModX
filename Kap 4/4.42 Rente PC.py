def p(t, r):
    return 7500/(1+r)**t


n = int(input("Hvor lang er perioden? "))
i = float(input("Hvor stor er renten? "))/100
total = 0

for t in range(0, n+1):
    total = p(t, i)
    print(round(total, 3))
