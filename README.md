# computational-ballistics
A simulation of bullet trajectories with increasing levels of accuracy and complexity.

## Table of Contents
- [1. Ideal model (no drag)](#1-ideal-model-no-drag)
- [2. Linear drag model](#2-linear-drag-model)

## 1. Ideal model (no drag)

We first assume an object of mass m that is launched from the point $(x_0,y_0)$ with speed V and angle $\theta$  
from Newton's second law, we know that

$$
\sum \vec{F_{ext}} = m\vec{a}
$$

assuming that the only force exerted on the object is its weight, so we can derive that :  

$$
\sum \vec{F_{ext}} = \vec{P} = m\vec{a}
$$ 

given that $\vec{P} = m\vec{g}$, we can conclude that :  

$$
m\vec{a} = m\vec{g}
$$

from this we can derive two equations :  

$$
\begin{cases}
a_x = 0 \\
a_y = -g
\end{cases}
$$

integrating with respect to time gives : 

$$
\begin{cases}
V_x = V_{x0} \\
V_y = -gt + V_{y0}
\end{cases}
$$

with : 

$$
\begin{cases}
V_{x0} = Vcos(\theta)\\
V_{y0} = Vsin(\theta)
\end{cases}
$$

integrating a second time gives us the position : 

$$
\begin{cases}
x =  Vcos(\theta)t + x_{0} \\
y = -\frac{g}{2}t^2 + Vsin(\theta)t + y_0
\end{cases}
$$

assuming that ground level is at y = 0, we can calculate the flight time by plugging y = 0 in our equation :

$$
0 = -\frac{g}{2}t_{flight}^2 + Vsin(\theta)t_{flight} + y_0
$$

which gives us : 

$$
t_{flight} = \frac{V\sin(\theta) \pm \sqrt{V^2\sin^2(\theta) + 2gy_0}}{g}
$$

taking the positive root, we have : 

$$
t_{flight} = \frac{V\sin(\theta) + \sqrt{V^2\sin^2(\theta) + 2gy_0}}{g}
$$

from these expressions, I wrote a code that represented the trajectory in Cartesian coordinates in "Ideal.py" and represented it on a graph with Numpy.

## 2. Linear drag Model

here we introduce linear drag to our model, since assuming no drag at such speeds is unrealistic.  
We start with a linear drag model for analytical tractability, even though quadratic drag is more physically accurate at bullet velocities. This serves as an intermediate step that can still be solved analytically before introducing the quadratic model, which requires numerical integration.
the updated equation gives us :  

$$
\sum \vec{F_{ext}} = \vec{P} - k\vec{V} = m\vec{a}
$$ 

from this we can again derive two differential equations : 

$$
\begin{cases}
ma_x = -kV_x \\
ma_y = -mg - kV_y
\end{cases}
$$

these differential equations are still analytically solvable. we will use these solutions as benchmarks for validating the accuracy of our numerical methods later.

we can rewrite these two equations as : 

$$
\begin{cases}
m\frac{dV_x}{dt} = -kV_x \\
m\frac{dV_y}{dt} = -mg - kV_y
\end{cases}
$$

i.e 

$$
\begin{cases}
\frac{dV_x}{dt} = -\frac{k}{m}V_x \\
\frac{dV_y}{dt} = -g - \frac{k}{m}V_y
\end{cases}
$$
the first equation is a homogeneous ODE, solving it yields : 

$$
V_x(t) = \Delta e^{-\frac{k}{m}t}
$$

the second one is a non homogeneous ODE, we must first solve the homogeneous equation  $\frac{dV_y}{dt} + \frac{k}{m}V_y = 0$, which is the same one as the first equation, therefore : 

$$
V_{yh}(t) = C e^{-\frac{k}{m}t}
$$

and by noticing that $V_{yp} : t \mapsto - \frac{m}{k}g$ is a particular solution of the equation, we can conclude that $V_y$ is such as : 

$$
V_{y}(t) = C e^{-\frac{k}{m}t} -\frac{m}{k}g
$$

which gives us these two equations : 

$$
\begin{cases}
V_x(t) = \Delta e^{-\frac{k}{m}t} \\
V_{y}(t) = C e^{-\frac{k}{m}t} -\frac{m}{k}g
\end{cases}
$$

knowing that : 

$$
\begin{cases}
V_{x0} = Vcos(\theta) \\
V_{y0} = Vsin(\theta)
\end{cases}
$$

we can conclude with the two speed equations : 

$$
\begin{cases}
V_x(t) = Vcos(\theta) e^{-\frac{k}{m}t} \\
V_{y}(t) = (Vsin(\theta) + \frac{m}{k}g) e^{-\frac{k}{m}t} -\frac{m}{k}g
\end{cases}
$$

integrating in respect to time yields the position equations bellow : 

$$
\begin{cases}
x(t) = -\frac{m}{k} Vcos(\theta) e^{-\frac{k}{m}t} + C \\
y(t) = -\frac{m}{k} (Vsin(\theta) + \frac{m}{k}g) e^{-\frac{k}{m}t} -\frac{m}{k}gt + C
\end{cases}
$$

and finally : 

$$
\begin{cases}
x(t) = \frac{m}{k} Vcos(\theta)(1 - e^{-\frac{k}{m}t}) + x_0  \\
y(t) = \frac{m}{k} (Vsin(\theta) + \frac{m}{k}g) (1- e^{-\frac{k}{m}t}) -\frac{m}{k}gt + y_0
\end{cases}
$$

These two equations will serve as a benchmark for testing the accuracy of Euler's method, since analytical solutions will no longer be possible once quadratic drag is introduced. Consequently, we will have to rely on numerical approximations of the solution.  
the implementation of this model as well as the comparison between Euler's approximation and the analytical solution can be found in "models/linear_drag.py"
