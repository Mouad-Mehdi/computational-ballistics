# computational-ballistics
A simulation of bullet trajectories with increasing levels of accuracy and complexity.

## Table of Contents
- [1. Ideal model (no drag)](#1-ideal-model-no-drag)
- [2. Linear drag model](#2-linear-drag-model)
- [3. Quadratic drag model](#3-quadratic-drag-model)

## 1. Ideal model (no drag)

The objective of this project being to model the trajectory of a bullet,we first assume an idealized object of mass (m) that is launched from the point $(x_0,y_0)$ with speed v and at angle $\theta$  
From Newton's second law, we know that

$$
\sum \vec{F_{ext}} = m\vec{a}
$$

Assuming that the only force exerted on the projectile is its weight , we can derive that   

$$
\sum \vec{F_{ext}} = \vec{P} = m\vec{a}
$$ 

Given that $\vec{P} = m\vec{g}$, we can conclude  

$$
m\vec{a} = m\vec{g}
$$

Thies yields the two component equations:  

$$
\begin{cases}
a_x = 0 \\
a_y = -g
\end{cases}
$$

Integrating with respect to time gives: 

$$
\begin{cases}
v_x = v_{x0} \\
v_y = -gt + v_{y0}
\end{cases}
$$

With: 

$$
\begin{cases}
v_{x0} = vcos(\theta)\\
v_{y0} = vsin(\theta)
\end{cases}
$$

Integrating once more yields the position: 

$$
\begin{cases}
x =  vcos(\theta)t + x_{0} \\
y = -\frac{g}{2}t^2 + vsin(\theta)t + y_0
\end{cases}
$$

Assuming that ground level is at y = 0, we can calculate the flight time by solving the equation y(t) = 0

$$
0 = -\frac{g}{2}t_{flight}^2 + vsin(\theta)t_{flight} + y_0
$$

Using the quadratic formula:

$$
t_{flight} = \frac{v\sin(\theta) \pm \sqrt{v^2\sin^2(\theta) + 2gy_0}}{g}
$$

We take the positive root, since time cannot be negative. The flight time is thus:

$$
t_{flight} = \frac{v\sin(\theta) + \sqrt{v^2\sin^2(\theta) + 2gy_0}}{g}
$$

Using these expressions, I wrote code that calculated the trajectory in "Ideal.py" and represented it in Cartesian coordinates with NumPy.


## 2. Linear drag Model


Considering the fact that air resistance plays an important role in the trajectory at high speeds, we will first introduce a linear drag model.
Even though quadratic drag is more physically accurate at high velocities, we start with a linear drag model mainly as a benchmark against which to test different numerical methods to solve ODEs, since obtaining analytical solutions will quickly become impractical.  

The updated equation gives us:  

$$
\sum \vec{F_{ext}} = \vec{P} - k\vec{v} = m\vec{a}
$$ 

Where k is the drag coeficient in $kgs^{-1}$

From this we can again derive two differential equations: 

$$
\begin{cases}
ma_x = -kv_x \\
ma_y = -mg - kv_y
\end{cases}
$$

These differential equations are still analytically solvable. We will use these solutions as benchmarks to validate the accuracy of our numerical methods later.

We can rewrite these two equations as: 

$$
\begin{cases}
m\frac{dv_x}{dt} = -kv_x \\
m\frac{dv_y}{dt} = -mg - kv_y
\end{cases}
$$

i.e., 

$$
\begin{cases}
\frac{dv_x}{dt} = -\frac{k}{m}v_x \\
\frac{dv_y}{dt} = -g - \frac{k}{m}v_y
\end{cases}
$$

The first equation is a homogeneous ODE; solving it yields: 

$$
v_x(t) = \Delta e^{-\frac{k}{m}t}
$$

The second one is a nonhomogeneous ODE. We must first solve the homogeneous equation  $\frac{dv_y}{dt} + \frac{k}{m}v_y = 0$; which is the same as the first equation, therefore: 

$$
v_{yh}(t) = C e^{-\frac{k}{m}t}
$$

Observing that $v_{yp} : t \mapsto - \frac{m}{k}g$ is a particular solution of the equation, we can conclude that $v_y$ is given by: 

$$
v_{y}(t) = C e^{-\frac{k}{m}t} -\frac{m}{k}g
$$

Which yields the velocity equations:

$$
\begin{cases}
v_x(t) = \Delta e^{-\frac{k}{m}t} \\
v_{y}(t) = C e^{-\frac{k}{m}t} -\frac{m}{k}g
\end{cases}
$$

Using the initial conditions: 

$$
\begin{cases}
v_{x0} = vcos(\theta) \\
v_{y0} = vsin(\theta)
\end{cases}
$$

We can conclude with the two completed speed equations: 

$$
\begin{cases}
v_x(t) = vcos(\theta) e^{-\frac{k}{m}t} \\
v_{y}(t) = (vsin(\theta) + \frac{m}{k}g) e^{-\frac{k}{m}t} -\frac{m}{k}g
\end{cases}
$$

Integrating with respect to time yields the position equations below: 

$$
\begin{cases}
x(t) = -\frac{m}{k} vcos(\theta) e^{-\frac{k}{m}t} + C \\
y(t) = -\frac{m}{k} (vsin(\theta) + \frac{m}{k}g) e^{-\frac{k}{m}t} -\frac{m}{k}gt + C
\end{cases}
$$

And finally: 

$$
\begin{cases}
x(t) = \frac{m}{k} vcos(\theta)(1 - e^{-\frac{k}{m}t}) + x_0  \\
y(t) = \frac{m}{k} (vsin(\theta) + \frac{m}{k}g) (1- e^{-\frac{k}{m}t}) -\frac{m}{k}gt + y_0
\end{cases}
$$

These analytical solutions provide a reference against which numerical methods such as Eulerand Runge–Kutta methods can be evaluated. we will have to rely on numerical approximations of the solutions once quadratic drag is introdced, since analytical solutions will no longer be easily obtained.

The implementation of this model as well as the comparison between Euler's method and the analytical solution can be found in "models/linear_drag.py"


## 3. Quadratic Drag Model


As explained previously, the linear drag model is inaccurate at high speeds. To accurately account for air resistance at bullet speeds, we consider quadratic drag, defined by

$$
F_d = -k \vec{v}|v|
$$

Where: 

$$
|v| = \sqrt{v_x^2 + v_y^2}
$$

When considering this drag force, Newton's second law becomes: 

$$
\sum \vec{F_{ext}} = \vec{P} - k\vec{v}|v| = m\vec{a}
$$ 

This yields the component equations: 

$$
\begin{cases}
\frac{dv_x}{dt} = - \frac{k}{m}|v|v_x \\
\frac{dv_y}{dt} = - \frac{k}{m}|v|v_y -g 
\end{cases}
$$ 

These equations form a system of coupled nonlinear, nonhomogeneous ordinary differential equations. Since no simple closed-form solution exists for the general case, Euler's method will be used to obtain a numerical approximation of the trajectory.



