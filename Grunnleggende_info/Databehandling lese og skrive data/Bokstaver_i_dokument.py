import os

if os.path.exists("Dokument.txt"):
    os.remove("Dokument.txt")
fil = open("Dokument.txt", "w", encoding="utf-8")
fil.write(
    "Jeg har ett helt dokument med flere ord, dette kan gå ganske bra. hvordan skal du skjønne dette når jeg lager en liste? men hvordan har du det da?")
fil.close()
fil = open("Dokument.txt", "r")

ord = []
bokstaver = []
for line in fil:
    bokstaver = line.strip()
    ord = line.split()

fil.close()

bokstaver = [kar for kar in bokstaver if kar != " "]
tegn = [kar for kar in bokstaver if kar in "!#¤%&/()=?`^*_:;>§@£${[]}+\¨'-.,<|´~"]

ftegn = list(dict.fromkeys(tegn))

print(f"Det er {len(ord)} ord, {len(bokstaver)} bokstaver, {len(tegn)} tegn og {len(ftegn)} forskjellige tegn.")
