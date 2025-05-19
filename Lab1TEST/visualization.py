import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import os


def animate_population(history, best_fitness, func, bounds, filename, resolution=100, fps=5, interval=200):
    """
    Створення GIF-анімації процесу пошуку з відображенням найкращого значення на кожій ітерації.
    history: список масивів популяції на кожній ітерації
    best_fitness: масив найкращих значень функції по ітераціям
    func: функція пристосованості
    bounds: [(x_min, x_max), (y_min, y_max)]
    filename: шлях до GIF-файлу
    resolution: роздільна здатність сітки для поверхні
    fps: кадрів за секунду при збереженні GIF
    interval: інтервал між кадрами в мілісекундах
    """
    x_min, x_max = bounds[0]
    y_min, y_max = bounds[1]
    x = np.linspace(x_min, x_max, resolution)
    y = np.linspace(y_min, y_max, resolution)
    X, Y = np.meshgrid(x, y)
    Z = np.vectorize(lambda xx, yy: func([xx, yy]))(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.6)
    scat = ax.scatter([], [], [], c='red')

    def update(frame):
        pop = history[frame]
        zs = np.array([func(ind) for ind in pop])
        scat._offsets3d = (pop[:, 0], pop[:, 1], zs)
        ax.set_title(f'Generation {frame+1}, Best = {best_fitness[frame]:.4f}')
        return scat,

    ani = animation.FuncAnimation(fig, update, frames=len(history), interval=interval)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    ani.save(filename, writer='pillow', fps=fps)
    plt.close(fig)


def plot_convergence(histories, labels, filename, max_iter=100):
    """
    Побудова графіка збіжності для кількох експериментів.
    histories: список масивів best_fitness по ітераціях
    labels: підписи для кожної кривої
    filename: шлях до зображення
    max_iter: максимальна кількість ітерацій для відображення по осі X
    """
    plt.figure()
    # Відрізати дані до max_iter
    x_vals = np.arange(1, max_iter+1)
    for hist, label in zip(histories, labels):
        plt.plot(x_vals, hist[:max_iter], label=label)
    plt.xlabel('Iteration')
    plt.ylabel('Best Fitness')
    plt.xlim(1, max_iter)
    # Встановити мітки по десятках
    plt.xticks(np.arange(0, max_iter+1, 10))
    plt.legend()
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename)
    plt.close()


if __name__ == "__main__":
    import pickle
    from fitness import FUNCTIONS
    from run_experiments import RESULTS_DIR, param_sets

    OUTPUT_DIR = os.path.join(RESULTS_DIR, 'images')
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for func_name, info in FUNCTIONS.items():
        func = info['func']
        bounds = info['bounds']

        histories = []
        labels = []
        for params in param_sets:
            pop_size = params['pop_size']
            child_size = params['child_size']
            mutation_rate = params['mutation_rate']
            fname = f"{func_name}_pop{pop_size}_child{child_size}_mut{mutation_rate}.pkl"
            filepath = os.path.join(RESULTS_DIR, fname)
            print(f"Loading results from {filepath}")
            with open(filepath, 'rb') as f:
                data = pickle.load(f)
            histories.append(data['best_fitness'])
            labels.append(f"pop{pop_size}_child{child_size}_mut{mutation_rate}")
            gif_file = os.path.join(OUTPUT_DIR, f"{func_name}_pop{pop_size}_child{child_size}_mut{mutation_rate}.gif")
            print(f"Animating population for {func_name} {pop_size}-{child_size}-{mutation_rate}")
            # Зменшений fps та збільшений інтервал сповільнюють анімацію
            animate_population(
                data['pop_history'], data['best_fitness'], func, bounds,
                gif_file, resolution=100, fps=5, interval=200
            )

        conv_file = os.path.join(OUTPUT_DIR, f"{func_name}_convergence.png")
        print(f"Plotting convergence for {func_name}")
        plot_convergence(histories, labels, conv_file)
    print("Visualization complete.")
