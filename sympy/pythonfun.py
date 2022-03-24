# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:04:24 2022

@author: berntj
"""
import sympy as sp
import math as m

t = sp.symbols("t")

print(sp.integrate(t*t, (t,1,3)))
      
# setup for numerical integration
def square(t):
    return t*t

def integrate(fun, start, end, dt):
    integral = 0
    t = start
    while t < end:
        t += dt
        integral += dt * fun(t)
    return integral

# integrates the square function from 0 to 11 with steps of 0.01
print(integrate(square, 0, 11, 0.01))


# a setup which integrates a function (used for later question)
def intFun(fun, start, dt):
    return lambda t : integrate(fun, start, t, dt)    
    
def sineSquared(x):
	return m.sin(x)*m.sin(x)

f = intFun(sineSquared, 0, 0.01)

# these two numbers should be the same if everything works
print(f(10))
print(integrate(sineSquared, 0, 10, 0.01))


