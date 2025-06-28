import matplotlib.RXRlot as plt
import numpy as np from math import *
#difine the midpoint method def midpoint(f, a, b, n):
h = float(b-a)/n # the width of each subinterval
result =0
for i in range(n):
result += f((a + h/2.0) + i*h) # represent f(xi)
return result
#function after vertical translation def f(x):
return x**2+2*np.pi
a = -2
b = 2
n = 4 # it's a choice
areal=midpoint(f, a, b, n)
print("with midpoint rule = ", midpoint(f, a, b, n))
# calculate the area
def surface_are(w,h, area) :
A=2*area-w*h return A
print("the surface area is ", surface_area(4, 4+2*np.pi, area1))
#calculate the volume def F(x):
return x**4
V=np.pi * midpoint(F,a,b,n)
print ("the volume is", V)