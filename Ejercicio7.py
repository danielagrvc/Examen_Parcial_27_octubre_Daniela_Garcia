from sympy import *
x=symbols("x")
y= symbols("y")
d= 4*x**9+1*x*y+1
v=x**3+x*y+7
def restar(d,v):
    resta=expand(d-v)
    print(resta)
def dividir(d,v):
    division=div(d/v)
    print(division)
restar(d,v)
dividir(d,v)


