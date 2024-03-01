import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import FuncAnimation

source = 0.5
sources = [-1, -0.5, 0, 0.5, 1]
shifts = [-10, -10, -50, -10, -10]
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
    C1 = np.sin((f+shifts[0])*0.1 + 2*np.pi*1*np.sqrt((X - sources[0])**2 + Y**2))
    C2 = np.sin((f+shifts[1])*0.1 + 2*np.pi*1*np.sqrt((X - sources[1])**2 + Y**2))
    C3 = np.sin((f+shifts[2])*0.1 + 2*np.pi*1*np.sqrt((X - sources[2])**2 + Y**2))
    C4 = np.sin((f+shifts[3])*0.1 + 2*np.pi*1*np.sqrt((X - sources[3])**2 + Y**2))
    C5 = np.sin((f+shifts[4])*0.1 + 2*np.pi*1*np.sqrt((X - sources[4])**2 + Y**2))
    Z = C1 + C2 + C3 + C4 + C5

    ax.imshow(Z,
              cmap = cmap,
              norm = norm)
    ax.plot(N/2*(1 + sources[0]/axlim), N/2, 'ro')
    ax.plot(N/2*(1 + sources[1]/axlim), N/2, 'ro')
    ax.plot(N/2*(1 + sources[2]/axlim), N/2, 'ro')
    ax.plot(N/2*(1 + sources[3]/axlim), N/2, 'ro')
    ax.plot(N/2*(1 + sources[4]/axlim), N/2, 'ro')

    ax.set_title(f'f = {f} Hz')
    ax.set_aspect('equal')
    ax.axis('off')

ani = FuncAnimation(fig = fig, func = update, frames = 100, interval = 10)

plt.show()
