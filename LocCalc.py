from typing import Any
import numpy as np
import matplotlib.pyplot as plt

from itertools import product

class sphere:
    def __init__(self, x:float, y:float, z:float, r:float=1) -> None:
        polars = np.linspace(0, np.pi, 19, dtype=np.float64)
        azimuths = np.linspace(0, 2*np.pi, 37, dtype=np.float64)

        radSet = np.array(list(product(polars, azimuths))).T

        sphereX = np.cos(radSet[1])*np.sin(radSet[0]).T * r     + x
        sphereY = np.sin(radSet[1])*np.sin(radSet[0]).T * r     + y
        sphereZ = np.cos(radSet[0]).T * r    + z

        self.center = (x, y, z)
        self.r = r
        self.scatter = (
            sphereX.reshape((19, 37)), 
            sphereY.reshape((19, 37)),
            sphereZ.reshape((19, 37))
            )
        self.A = 2*x
        self.B = 2*y
        self.C = 2*z
        self.D = self.r**2 - (self.A**2 + self.B**2 + self.C**2)/4
    
    def __call__(self, *args: Any, **kwds: Any) -> tuple:
        return self.scatter

def intersection(a:sphere, b:sphere):
    print(
        a.A - b.A,
        a.B - b.B,
        a.C - b.C,
        a.D - b.D
    )



sphere1 = sphere(20, 3, 1, r=5)
sphere2 = sphere(25, 0, 0, r=4)

intersection(sphere1, sphere2)

fig, ax = plt.subplots(figsize=(5, 5), 
                       subplot_kw={"projection":"3d"})
ax.set_box_aspect((1, 1, 1))
# ax.plot_surface(*sphere(20, 0, 0, r=5), 
                # alpha=0.3)
ax.plot_wireframe(*sphere1(),
                  alpha=0.8)
ax.plot_wireframe(*sphere2(),
                  alpha=0.8)

plt.show()