def f(x):
    return 2*x + 1

def Newton(f,x,h):
    fder = (f(x+h)-f(x))/(h)
    return fder

h = [10**-i for i in range(1,17)]

for i in range(0, len(h)):
    print(f"for h = {h[i]} : {Newton(f, 1, h[i])}")
