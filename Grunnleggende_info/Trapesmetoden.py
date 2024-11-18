from Rektangelmetoden import n, f

def trapesmetoden(a,b):
    h = (b - a) / n
    total = (f(a) + f(b)) / 2.0
    for k in range(1,n):
        total += f(a + k*h)
    return h*total

if __name__ == "__main__":
    print(f"trapesmetoden: {trapesmetoden(0, 5)}")
