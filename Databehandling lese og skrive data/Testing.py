fil = open("Testing.txt", "w", encoding="utf-8")
fil.write("Jeg har ett helt dokument med flere ord, dette kan gå ganske bra. hvordan skal du skjønne dette når jeg lager en liste?")
fil.close()
fil = open("Testing.txt", "r")

antall = []
for rad in fil:
    ord = rad.split()
    antall.extend(ord)

fil.close()
print(antall)
print(len(antall))