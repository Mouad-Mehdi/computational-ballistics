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
    state = initial.copy()
    points = []
    times = []
    while t < b :
        points.append(state)
        times.append(t)
        state = state + h*f(t,state)
        t = t + h
    return np.array(times), np.array(points)


# An implementation of RK4 :
def rk4(f,a,b,h,initial):
    t = a
    state = initial.copy()
    points = []
    times = []
    while t < b :
        points.append(state)
        times.append(t)
        k1 = f(t, state)
        k2 = f(t + h/2, state + (h/2) * k1)
        k3 = f(t + h/2, state + (h/2) * k2)
        k4 = f(t + h, state + h*k3)
        state = state + (h/6)*(k1 +2*k2 + 2*k3 + k4)
        t = t + h
    return np.array(times), np.array(points)

# Reserved for future Monte Carlo extension (not yet used)
# Ploting the Monte Carlo simulation, state vector is [vx, vy, x, y] :
def monte_carlo_plot(samples,x0,y0):
    plt.grid(True)
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.axis('equal')
    plt.scatter(x0, y0, color="red", label="Launch point")
    plt.title("Monte Carlo simulations")
    for trajectory in samples :
        X = trajectory[:,2]
        Y = trajectory[:,3]
        mask= Y >= 0
        X = X[mask]
        Y = Y[mask]
        plt.plot(X, Y, color="blue", alpha=0.2)
    plt.legend()
    plt.show()

