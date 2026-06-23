import matplotlib.pyplot as plt

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

# Implementing Euler's aproximation to get a set of points representing V([a,b]) 
# given a certain ODE dV/dt = f(V), a step size 'h' , and an initial condition V(0) = z0  :
def euler(f, a, b, h, z0):
    t = a
    z = z0
    points = []
    while t < b :
        points.append(z)
        z = z + h*f(z)
        t = t + h
    return np.array(points)

# Implementing Euler's approximation to compute the integral of a function
# given the derivative values, a step size h (the same one used to obtain
# the sample), and an initial value z0.
def euler_integral(derivatives, h, z0):
    z = z0
    points = []
    for i in derivatives:
        points.append(z)
        z = z +h*i
