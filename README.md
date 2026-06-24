# computational-ballistics
A simulation of bullet trajectories with increasing levels of accuracy and complexity.

## Table of Contents
- [1. Ideal model (no drag)](#1-ideal-model-no-drag)
- [2. Linear drag model](#2-linear-drag-model)

## 1. Ideal model (no drag)

We first assume an object of mass m that is launched from the point $(x_0,y_0)$ with speed v and angle $\theta$  
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
v_x = v_{x0} \\
v_y = -gt + v_{y0}
\end{cases}
$$

with : 

$$
\begin{cases}
v_{x0} = vcos(\theta)\\
v_{y0} = vsin(\theta)
\end{cases}
$$

integrating a second time gives us the position : 

$$
\begin{cases}
x =  vcos(\theta)t + x_{0} \\
y = -\frac{g}{2}t^2 + vsin(\theta)t + y_0
\end{cases}
$$

assuming that ground level is at y = 0, we can calculate the flight time by plugging y = 0 in our equation :

$$
0 = -\frac{g}{2}t_{flight}^2 + vsin(\theta)t_{flight} + y_0
$$

which gives us : 

$$
t_{flight} = \frac{v\sin(\theta) \pm \sqrt{v^2\sin^2(\theta) + 2gy_0}}{g}
$$

taking the positive root, we have : 

$$
t_{flight} = \frac{v\sin(\theta) + \sqrt{v^2\sin^2(\theta) + 2gy_0}}{g}
$$

from these expressions, I wrote a code that represented the trajectory in Cartesian coordinates in "Ideal.py" and represented it on a graph with Numpy.

## 2. Linear drag Model

here we introduce linear drag to our model, since assuming no drag at such speeds is unrealistic.  
We start with a linear drag model for analytical tractability, even though quadratic drag is more physically accurate at bullet velocities. This serves as an intermediate step that can still be solved analytically before introducing the quadratic model, which requires numerical integration.
the updated equation gives us :  

$$
\sum \vec{F_{ext}} = \vec{P} - k\vec{v} = m\vec{a}
$$ 

from this we can again derive two differential equations : 

$$
\begin{cases}
ma_x = -kv_x \\
ma_y = -mg - kv_y
\end{cases}
$$

these differential equations are still analytically solvable. we will use these solutions as benchmarks for validating the accuracy of our numerical methods later.

we can rewrite these two equations as : 

$$
\begin{cases}
m\frac{dv_x}{dt} = -kv_x \\
m\frac{dv_y}{dt} = -mg - kv_y
\end{cases}
$$

i.e 

$$
\begin{cases}
\frac{dv_x}{dt} = -\frac{k}{m}v_x \\
\frac{dv_y}{dt} = -g - \frac{k}{m}v_y
\end{cases}
$$
the first equation is a homogeneous ODE, solving it yields : 

$$
v_x(t) = \Delta e^{-\frac{k}{m}t}
$$

the second one is a non homogeneous ODE, we must first solve the homogeneous equation  $\frac{dv_y}{dt} + \frac{k}{m}v_y = 0$, which is the same one as the first equation, therefore : 

$$
v_{yh}(t) = C e^{-\frac{k}{m}t}
$$

and by noticing that $v_{yp} : t \mapsto - \frac{m}{k}g$ is a particular solution of the equation, we can conclude that $v_y$ is such as : 

$$
v_{y}(t) = C e^{-\frac{k}{m}t} -\frac{m}{k}g
$$

which gives us these two equations : 

$$
\begin{cases}
v_x(t) = \Delta e^{-\frac{k}{m}t} \\
v_{y}(t) = C e^{-\frac{k}{m}t} -\frac{m}{k}g
\end{cases}
$$

knowing that : 

$$
\begin{cases}
v_{x0} = vcos(\theta) \\
v_{y0} = vsin(\theta)
\end{cases}
$$

we can conclude with the two speed equations : 

$$
\begin{cases}
v_x(t) = vcos(\theta) e^{-\frac{k}{m}t} \\
v_{y}(t) = (vsin(\theta) + \frac{m}{k}g) e^{-\frac{k}{m}t} -\frac{m}{k}g
\end{cases}
$$

integrating in respect to time yields the position equations bellow : 

$$
\begin{cases}
x(t) = -\frac{m}{k} vcos(\theta) e^{-\frac{k}{m}t} + C \\
y(t) = -\frac{m}{k} (vsin(\theta) + \frac{m}{k}g) e^{-\frac{k}{m}t} -\frac{m}{k}gt + C
\end{cases}
$$

and finally : 

$$
\begin{cases}
x(t) = \frac{m}{k} vcos(\theta)(1 - e^{-\frac{k}{m}t}) + x_0  \\
y(t) = \frac{m}{k} (vsin(\theta) + \frac{m}{k}g) (1- e^{-\frac{k}{m}t}) -\frac{m}{k}gt + y_0
\end{cases}
$$

These two equations will serve as a benchmark for testing the accuracy of Euler's method, since analytical solutions will no longer be easily obtained once quadratic drag is introduced. Consequently, we will have to rely on numerical approximations of the solution.  
the implementation of this model as well as the comparison between Euler's approximation and the analytical solution can be found in "models/linear_drag.py"

## 3. Quadratic drag

As explained previously, the linear drag model is inaccurate at high speeds. To accurately account for air resistance at bullet speeds, we consider quadratic drag, defined by

$$
F_d = -k \vec{v}|v|
$$

Where 

$$
|v| = \sqrt{v_x^2 + v_y^2}
$$

When considering this drag force, Newton's second law becomes 

$$
\sum \vec{F_{ext}} = \vec{P} - k\vec{v}|v| = m\vec{a}
$$ 

This yields the component equations 

$$
\begin{cases}
\frac{dv_x}{dt} = - \frac{k}{m}|v|v_x \\
\frac{dv_y}{dt} = - \frac{k}{m}|v|v_y -g 
\end{cases}
$$ 

These equations form a system of coupled nonlinear, nonhomogeneous ordinary differential equations. Since no simple closed-form solution exists for the general case, Euler's method will be used to obtain a numerical approximation of the trajectory.



