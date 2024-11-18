from pylab import *

# Fysiske størrelser
g = 9.81        # Tyngdeakselerasjon i m/s^2
m = 0.5         # Masse i Kg
k = 0.2         # Luftmotstandskoeffisienten i Nsm^-2

# Tidsintervaller
N = 100000      # Antall intervaller
tid = 2         # Antall Sekunder
dt = tid/N      # Tidssteget

# Matriser
a = zeros(N)    # askelerasjon i m/s^2
v = zeros(N)    # hastighet i m/s
s = zeros(N)    # posisjon i m
t = zeros(N)    # tid i s

# initialbetingelser
v[0] = 0        # startfart 0 m/s
s[0] = 0        # Startposisjon 0

# Eulers metode
for i in range(N-1):
    a[i] = g - (k*v[i]**2)/m # Likning 8.12
    v[i + 1] = v[i] + a[i] * dt
    s[i + 1] = s[i] + v[i] * dt
    t[i + 1] = t[i] + dt

# Plotting
subplot(3,1,1)
plot(t,a,"b-")
title("akselerasjon")
xlabel("Tid")
ylabel("akselerasjon")

subplot(3,1,2)
plot(t,v,"r-")
title("hastighet")
xlabel("tid")
ylabel("hastighet")

subplot(3,1,3)
plot(t,s,"g-")
title("Strekning")
xlabel("tid")
ylabel("strekning")
show()
