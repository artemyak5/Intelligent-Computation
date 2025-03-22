import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation

def plot_convergence(conv_history, title, filename):
    plt.figure(figsize=(8, 6))
    plt.plot(conv_history, linestyle='-', linewidth=2)
    plt.xlabel("Ітерація")
    plt.ylabel("Найкраще значення функції")
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

def animate_3d(func, bounds, pos_history, conv_history, title, gif_filename):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    x_vals = np.linspace(bounds[0, 0], bounds[0, 1], 100)
    y_vals = np.linspace(bounds[1, 0], bounds[1, 1], 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = np.empty_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = func(np.array([X[i, j], Y[i, j]]))

    ax.plot_surface(X, Y, Z, cmap=cm.viridis, alpha=0.6)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("f(x, y)")

    scatter = ax.scatter([], [], [], color='r', s=50)

    def update(frame):
        pts = np.array(pos_history[frame])
        z_vals = np.array([func(pt) for pt in pts])
        scatter._offsets3d = (pts[:, 0], pts[:, 1], z_vals)
        ax.set_title(f"{title} - Ітерація {frame+1} | Найкраще: {conv_history[frame]:.4f}")
        return scatter,

    ani = FuncAnimation(fig, update, frames=len(pos_history), interval=200, blit=False)
    ani.save(gif_filename, writer='pillow')
    plt.close(fig)
