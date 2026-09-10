import math

L = 0.0
R = 1.0

while (R - L) > 0.0001:
    cor = (L + R) / 2
    
    if (1 - 0.4*cor**2) ** 0.5 - math.asin(cor) > 0:
        L = cor
    else:
        R = cor
        
    print(cor)
print('-----------------')

def f(x):
    return math.sqrt(1 - 0.4 * x**2) - math.asin(x)

a = 0.0
b = 1.0
eps = 0.0001

k = 0
x_k = 0.0
x_prev = 0.0

while True:
    k += 1
    x_prev = x_k
    
    fa = f(a)
    fb = f(b)
    x_k = a - fa * (b - a) / (fb - fa)
    fx = f(x_k)
    
    if abs(fx) < 0.0001:
        break
        
    if fx * fb > 0:
        b = x_k
    else:
        a = x_k

print(x_k)
