fil = open("bevegelse.txt", "r")
fil.readline()
t = []
s = []

for rad in fil:
    data = rad.split()
    t.append(float(data[0]))
    s.append(float(data[1]))
fil.close()

print(t)
print(s)