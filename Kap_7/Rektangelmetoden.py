import numpy as np
def f(x):
    return np.e**x
n = 100

def rektangelmetoden(a, b):
    total = 0.0
    h = (b-a)/n
    for k in range(0, n):
        total += f(a + (k*h))
    areal = h*total
    return areal

if __name__ == "__main__":
    print(f"rektangelmetoden: {rektangelmetoden(0, 5)}")

