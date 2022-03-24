import sympy as sp
import math as m

# t = sp.symbols("t")

def integrate(fun, start, end, dt):
    integral = 0
    t = start
    while t < end:
        t += dt
        integral += dt * fun(t)
    return integral


# a setup which integrates a function (used for later question)
def intFun(fun, start, dt):
    return lambda t : integrate(fun, start, t, dt) 

def a(x):
    return m.sin((x**3)+(x**2))

x = sp.symbols("x") # må kanskje øverst
t = sp.symbols("t")
f = intFun(a, 0, 0.01)
print(integrate(f, 0, 3, 0.05))
