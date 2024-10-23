def rektangelmetoden(a, b, n):
    total = 0.0
    h = (b-a)/n
    for k in range(0, n):
        total += f(a + (k*h))
    areal = h*total
    return areal

if __name__ == "__main__":

    print(rektangelmetoden(0,5,1000000))
