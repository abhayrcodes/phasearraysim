import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import FuncAnimation

source = 0.5
sources = [-source, source]
axlim = max(sources)*2 + 1
N = 1000

x = np.linspace(-axlim, axlim, N)
y = np.linspace(-axlim, axlim, N)
X, Y = np.meshgrid(x, y)

norm = plt.Normalize(-2, 2)
cmap = LinearSegmentedColormap.from_list('', ['black', 'white', 'black'])
fig, ax = plt.subplots()

def update(f):
    ax.cla()
    C1 = np.sin(2*np.pi*f*np.sqrt((X - sources[0])**2 + Y**2))
    C2 = np.sin(2*np.pi*f*np.sqrt((X - sources[1])**2 + Y**2))
    Z = C1 + C2

    ax.imshow(Z,
              cmap = cmap,
              norm = norm)
    ax.plot(N/2*(1 + source/axlim), N/2, 'ro')
    ax.plot(N/2*(1 - source/axlim), N/2, 'ro')

    ax.set_title(f'f = {f} Hz')
    ax.set_aspect('equal')
    ax.axis('off')

ani = FuncAnimation(fig = fig, func = update, frames = 11, interval = 100)

plt.show()
