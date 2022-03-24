import sympy as sp
import math as m

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

'''
def x_cord(t):
    return 100 + t**2

def y_cord(t):
    return 200 + 3*(t**3)
'''
def x_vel(t):
    return 10

def y_vel(t):
    return 20

print(intFun(x_vel, 0, 1.0/60.0)(5) + 100)
print(intFun(y_vel, 0, 1.0/60.0)(5) + 200)
'''
t = sp.symbols("t")
x_cord = t**2 + 100
y_cord = sp.S(3)*(t**3) + 200
print(sp.diff(x_cord, t).subs(t, 3))
print(sp.diff(y_cord, t).subs(t, 3))
'''

