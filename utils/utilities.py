import matplotlib.pyplot as plt
import numpy as np

# Function that plots the bullet trajectory given the initial conditions :
def plot_trajectory(X, Y, x0 ,y0, title):
    plt.grid(True)
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.axis('equal')
    plt.scatter(x0, y0, color="red", label="Launch point")
    plt.plot(X,Y,color="blue")
    plt.title(title)
    plt.legend()
    plt.show()

# Function that plots the bullet trajectory given the initial conditions, and compares it with the Euler's approximation of the trajectory
def plot_trajectory_comp(X, Y, X_euler, Y_euler, x0 ,y0, title):
    plt.grid(True)
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.axis('equal')
    plt.scatter(x0, y0, color="red", label="Launch point")
    plt.plot(X,Y,color="blue",label="Trajectory")
    plt.plot(X_euler,Y_euler,color="green",label="Euler's approximation")
    plt.title(title)
    plt.legend()
    plt.show()

# Implementing Euler's aproximation to get a set of points representing V([a,b]) 
# given a certain ODE dV/dt = f(V), a step size 'h' , and an initial condition V(0) = z0  :
def euler(f, a, b, h, initial):
    t = a
    value = initial
    points = []
    while t < b :
        points.append(value)
        value = value + h*f(value)
        t = t + h
    return np.array(points)

# Implementing Euler's approximation to compute the integral of a function
# given the derivative values, a step size h (the same one used to obtain
# the sample), and an initial value z0.
def euler_integral(derivatives, h, initial):
    value = initial
    points = []
    for derivative in derivatives:
        points.append(value)
        value = value +h*derivative
    return np.array(points)

# a function used to get sample points for x(t)/y(t) given an ODE dV/dt = f(V),
# two initial conditions v0 and z0, and a step size h.
def position_from_velocity_ode(f, a, b, h, initial_v, initial_pos):
    Velocity = euler(f, a, b, h, initial_v)
    positions = euler_integral(Velocity, h, initial_pos)
    return positions

