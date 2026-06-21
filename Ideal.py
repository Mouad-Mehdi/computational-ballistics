import matplotlib.pyplot as plt 
import numpy as np

#this code assumes a lanch point of (0,Y0), with speed V and angle theta.

g = 9.8 # gravity constant
V = 400 # launch speed
theta = np.radians(45) # launch angle
Y0 = 1000 # initial height
t_flight = (V*np.sin(theta) + np.sqrt((V*np.sin(theta))**2 + 2*g*Y0)) / g # calculated flight time

T = np.linspace(0,t_flight,1000)

def y(t) : # vertical component
    return (-g/2)*t**2 + V*np.sin(theta)*t + Y0

def x(t) : # horizontal component
    return V*np.cos(theta)*t

X = x(T) 
Y = y(T)


plt.grid(True)
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.axis('equal')
plt.scatter(0, Y0, color="red", label="Launch point") # plotting the launch point
plt.plot(X,Y,color="blue") # plotting the trajectory
plt.title("Idealized trajectory")
plt.legend()
plt.show()