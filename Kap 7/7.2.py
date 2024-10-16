def f(x):
    return 5*x*5 + 3*x + 3

def derivert(f, x):
    fder = (f(x + 10**-7) - f(x)) / 10**-7
    print(fder)
    return;

derivert(f, 1)