import numpy as np
import utils.utilities as ut


# Physical parameters : 
g = 9.8 # Gravitational acceleration
m = 0.0162 # Mass of the object in kg
k = 1e-5 # Drag coefficient

# Initial conditions : 
v = 850 # Launch speed in m/s
theta = np.radians(34) # Launch angle 
x0 = 0 # Initial
y0 = 0 # Initial height

# State vector is of the form [vx, vy, x, y]
initial_state = np.array([v*np.cos(theta), v*np.sin(theta), x0, y0])

# Numerical solvers parameters :
h = 0.01

# Auxiliary function to numercially solve the ODE :
def f(t,state):
    vx, vy, x, y = state
    speed = np.sqrt(vx**2 + vy**2)
    return np.array([(-k/m)*speed*vx , (-k/m)*speed*vy -g, vx, vy])

# A generous upperbound for the flight time, given that drag can only reduce it : 
t_max_guess = (v*np.sin(theta) + np.sqrt((v*np.sin(theta))**2 + 2*g*y0)) / g 

# Calculating the array of state vectors using Euler's method
states_euler = ut.euler(f,0,t_max_guess,h,initial_state)[1]

# Calculating the array of state vectors using RK4
states_rk4 = ut.rk4(f,0,t_max_guess,h,initial_state)[1]

# Extracting the coordinates from the state vector array
X_euler = states_euler[:,2]
X_rk4 = states_rk4[:,2]
Y_euler = states_euler[:,3]
Y_rk4 = states_rk4[:,3]

# Only taking the positions above ground
mask_euler = Y_euler >= 0
mask_rk4 = Y_rk4 >= 0

ut.plot_trajectory_comp(X_euler[mask_euler], 
                        Y_euler[mask_euler], 
                        X_rk4[mask_rk4], 
                        Y_rk4[mask_rk4], 
                        x0, 
                        y0, 
                        "y(x) under quadratic drag", 
                        "Euler's approximation", 
                        "RK4 approximation")
