import matplotlib.pyplot as plt 
import numpy as np
from scipy.optimize import brentq
from utils.utilities import plot_trajectory
from utils.utilities import euler_vectorial
from utils.utilities import euler_integral

# Physical parameters : 
g = 9.8 # Gravitational acceleration
m = 0.0162 # Mass of the object in kg
k = 1e-5 # Drag coefficient

# Initial conditions : 
v = 850 # Launch speed in m/s
theta = np.radians(34) # Launch angle 
x0 = 0 # Initial
y0 = 0 # Initial height

# Euler's approximation parameters :
h = 0.001

# Auxiliary function to numercially solve the ODE :
def f(state):
    vx, vy = state
    return np.array([(-k/m)*np.sqrt(vx**2 + vy**2)*vx , (-k/m)*np.sqrt(vx**2 + vy**2)*vy -g])

# A generous upperbound for the flight time, given that drag can only reduce it : 
t_max_guess = (v*np.sin(theta) + np.sqrt((v*np.sin(theta))**2 + 2*g*y0)) / g 

states = euler_vectorial(f,0,t_max_guess,h,np.array([v*np.cos(theta),v*np.sin(theta)]))

# Calculating an approximation of x(flight_points) using Euler's method
X_euler = euler_integral(states[:,0],h,x0)

# Calculating an approximation of y(flight_points) using Euler's method, given that dv_y/dt = (-k/m)*v_y -g
Y_euler = euler_integral(states[:,1],h,y0)

# Only taking the positions above ground
mask = Y_euler >= 0

plot_trajectory(X_euler[mask], Y_euler[mask], x0, y0, "Bullet trajectory under quadratic drag")
