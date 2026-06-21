# computational-ballistics
A simulation of bullet trajectories with increasing levels of accuracy and complexity.  
We first assume an object of mass m that is launched from the point $(x_0,y_0)$ with speed V and angle $\theta$  
from Newton's second law, we know that

$$
\sum \vec{Fext} = m\vec{a}
$$

assuming that the only force exerted on the object is its weight, so we can derive that :  

$$
\sum \vec{Fext} = \vec{P} = m\vec{a}
$$ 

given that $\vec{P} = m\vec{g}$, we can conclude that :  

$$
\large{m\vec{a} = m\vec{g}}
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

from these expressions, I wrote a code that represented the trajectory y(x) in "Ideal.py" and represented it on a graph with Numpy.
