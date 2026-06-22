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