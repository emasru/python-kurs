import sympy as sp
import math as m
      
# setup for numerical integration
def square(t):
    return t*t

def cube(t):
    return t*t*t

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
    
def sineSquared(x):
	return m.sin(x)*m.sin(x)

# f = intFun(sineSquared, 0, 0.01)

# these two numbers should be the same if everything works
# print(f(10))
# print(integrate(sineSquared, 0, 10, 0.01))
# print(integrate(square, 1, 3, 0.1))
# print(integrate(m.sin, 0, 2*m.pi, 0.01))

t = sp.symbols("t")
x = sp.symbols("x")
# f = sp.S(4)*(x**3)
f = sp.S(5)*(x**4)

print(sp.integrate(f, (x, 4, t)))
print(sp.integrate(f, (x, 3, t)))