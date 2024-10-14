def f(x):
    return x**2

def rektangelmetoden(f, a, b, n):
    total = 0.0
    h = (b-a)/n
    for k in range(0, n):
        total = total + f(a + (k*h))
    Areal = h*total
    return Areal

print(rektangelmetoden(f, 0, 5, 10000))
print((1/3)*(5**3))