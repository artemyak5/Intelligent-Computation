import os
from algorithm import PSO
from visualization import plot_convergence, animate_3d

def run_experiment(func, bounds, expected, description, output_dir,
                   swarm_size=50, iterations=100,
                   w_max=0.9, w_min=0.4, c1=1.0, c2=2.5,
                   random_limits=None, break_faster=False, epsilon=1e-6, cnt_max=3,
                   clamp_velocity=1.0):
    """
    Запуск алгоритму PSO з заданими параметрами і збереження результатів.
    """
    optimizer = PSO(
        func, bounds,
        swarm_size=swarm_size,
        iterations=iterations,
        w_max=w_max,
        w_min=w_min,
        c1=c1,
        c2=c2,
        random_limits=random_limits,
        break_faster=break_faster,
        epsilon=epsilon,
        cnt_max=cnt_max,
        clamp_velocity=clamp_velocity
    )
    best_val, best_pos, conv_history, pos_history = optimizer.optimize()

    print(f"Оптимізація: {description}")
    print(f"  Найкраще значення: {best_val}")
    print(f"  Положення: {best_pos}")
    print(f"  Очікуване: {expected}")

    conv_filename = os.path.join(output_dir, f"convergence_{description.replace(' ', '_')}.png")
    gif_filename = os.path.join(output_dir, f"animation_{description.replace(' ', '_')}.gif")

    # Побудова графіка конвергенції
    plot_convergence(conv_history, f"Конвергенція - {description}", conv_filename)
    # Створення 3D-анімації
    animate_3d(func, bounds, pos_history, conv_history, f"PSO - {description}", gif_filename)

    print(f"  Збережено графік: {conv_filename}")
    print(f"  Збережено анімацію: {gif_filename}")
