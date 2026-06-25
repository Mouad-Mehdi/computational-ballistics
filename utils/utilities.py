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

# Function that plots the bullet trajectory given the initial conditions,
# and compares it with another trajectory
def plot_trajectory_comp(X1, Y1, X2, Y2, x0 ,y0, title, plot1, plot2):
    plt.grid(True)
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.axis('equal')
    plt.scatter(x0, y0, color="red", label="Launch point")
    plt.plot(X1,Y1,color="blue",label=plot1)
    plt.plot(X2,Y2,color="orange",label=plot2)
    plt.title(title)
    plt.legend()
    plt.show()


# Redifining a new function implementing Euler's method with a function taking 
# the state vector instead of an integer as parameter.
def euler(f, a, b, h, initial):
    t = a
    state = initial
    points = []
    while t < b :
        points.append(state)
        state = state + h*f(state)
        t = t + h
    return np.array(points)

# An implementation of RK4 :
def rk4(f,a,b,h,initial):
    t = a
    state = initial
    points = []
    while t < b :
        points.append(state)
        k1 = f(state)
        k2 = f(state + (h/2) * k1)
        k3 = f(state + (h/2) * k2)
        k4 = f(state + h*k3)
        state = state + (h/6)*(k1 +2*k2 + 2*k3 + k4)
        t = t + h
    return np.array(points)
