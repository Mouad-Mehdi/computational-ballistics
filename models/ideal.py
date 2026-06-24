import matplotlib.pyplot as plt 
import numpy as np
from utils.utilities import plot_trajectory

# Physical parameters : 
g = 9.8 # Gravitational acceleration

# Initial conditions : 
v = 850 # Launch speed in m/s
theta = np.radians(34) # Launch angle 
x0 = 0 # Initial
y0 = 0 # Initial height

def y(t) : # vertical component
    return (-g/2)*t**2 + v*np.sin(theta)*t + y0

def x(t) : # horizontal component
    return v*np.cos(theta)*t + x0

# Calculating the landing time at ground level (y=0)
t_flight = (v*np.sin(theta) + np.sqrt((v*np.sin(theta))**2 + 2*g*y0))/g 

flight_points = np.linspace(0,t_flight,1000)

X = x(flight_points) 
Y = y(flight_points)

plot_trajectory(X, Y, x0, y0, "Ideal trajectory")

