"""python program to plot sinx,cosx functions"""
import matplotlib.pyplot as plt
from numpy import linspace,sin,cos,pi 
x=linspace(0,2*pi,50)
y=sin(x)
z=cos(x)
plt.stem(x,y,linefmt="k",markerfmt="rd")
plt.stem(x,z,linefmt="g",markerfmt="y")
plt.plot(x,y)
plt.plot(x,z)
plt.show 