import matplotlib.pyplot as plt 
import numpy as np
from scipy.optimize import brentq
from utils.utilities import plot_trajectory

# Physical parameters : 
g = 9.8 # Gravitational acceleration
m = 1 # Mass of the object in kg
k = 0.5 # Drag coefficient

# Initial conditions : 
v = 400 # Launch speed in m/s
theta = np.radians(45) # Launch angle 
x0 = 0 # Initial
y0 = 0 # Initial height


def y(t) : # Vertical positional equation
    return y0 + (m/k)*(v*np.sin(theta) + m*g/k)*(1 - np.exp(-k*t/m)) -m*g*t/k

def x(t) : # Horizontal positional equation 
    return x0 + (m*v*np.cos(theta)/k)*(1-np.exp(-k*t/m))

# A generous upperbound for the flight time since the drag can only reduce it : 
t_max_guess = (v*np.sin(theta) + np.sqrt((v*np.sin(theta))**2 + 2*g*y0)) / g 
# Calculating the landing time at ground level (y=0)
t_flight = brentq(y,1,t_max_guess) 

flight_points = np.linspace(0,t_flight,1000)

X = x(flight_points)
Y = y(flight_points)

plot_trajectory(X, Y, x0, y0, "linear drag trajectory")

