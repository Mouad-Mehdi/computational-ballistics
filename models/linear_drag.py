import numpy as np
from scipy.optimize import brentq
import utils.utilities as ut


# Physical parameters : 
g = 9.8 # Gravitational acceleration
m = 0.0162 # Mass of the object in kg
k = 0.001 # Drag coefficient

# Initial conditions : 
v = 850 # Launch speed in m/s
theta = np.radians(34) # Launch angle 
x0 = 0 # Initial
y0 = 0 # Initial height

# State vector is of form [vx, vy, x, y]
initial_state = np.array([v*np.cos(theta), v*np.sin(theta), x0, y0])

# Numerical solvers parameters :
h = 0.1

def y(t) : # Vertical positional equation
    return y0 + (m/k)*(v*np.sin(theta) + m*g/k)*(1 - np.exp(-k*t/m)) -m*g*t/k

def x(t) : # Horizontal positional equation 
    return x0 + (m*v*np.cos(theta)/k)*(1-np.exp(-k*t/m))

# A generous upperbound for the flight time since the drag can only reduce it : 
t_max_guess = (v*np.sin(theta) + np.sqrt((v*np.sin(theta))**2 + 2*g*y0)) / g 
# Calculating the landing time at ground level (y=0)
t_flight = brentq(y,1e-3,t_max_guess) 

# Auxiliary function
def f(t,state):
    vx, vy, x, y = state
    return np.array([(-k/m)*vx, (-k/m)*vy -g, vx, vy ])

# Calculating the state array and the time array using Euler's approximation
flight_points, states = ut.euler(f,0,t_flight,h,initial_state)

# Extracting the coordinates :
X_euler = states[:,2]
Y_euler = states[:,3]


X = x(flight_points)
Y = y(flight_points)

ut.plot_trajectory_comp(X, Y, X_euler, Y_euler, x0, y0, "linear drag trajectory","Analytical solution","Euler's approximation")


