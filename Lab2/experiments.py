import os
import matplotlib.pyplot as plt
from algorithm import PSO

def compare_experiments(func, bounds, exp_params, description, output_dir,
                        random_limits=None, break_faster=False, epsilon=1e-6, cnt_max=3,
                        clamp_velocity=1.0):
    """
    Порівнює різні набори параметрів (exp_params) для однієї функції.
    exp_params – список словників, кожен з яких має:
       {
         'swarm_size': ...,
         'iterations': ...,
         'w_max': ...,
         'w_min': ...,
         'c1': ...,
         'c2': ...,
         'label': ...
       }
    """
    convergence_curves = []
    labels = []

    for param in exp_params:
        pso = PSO(
            func, bounds,
            swarm_size=param['swarm_size'],
            iterations=param['iterations'],
            w_max=param.get('w_max', 0.9),
            w_min=param.get('w_min', 0.4),
            c1=param.get('c1', 1.0),
            c2=param.get('c2', 2.5),
            random_limits=random_limits,
            break_faster=break_faster,
            epsilon=epsilon,
            cnt_max=cnt_max,
            clamp_velocity=clamp_velocity
        )
        best_val, best_pos, conv_history, _ = pso.optimize()
        convergence_curves.append(conv_history)
        labels.append(f"{param['label']} (min={best_val:.6f})")

    plt.figure(figsize=(10,6))
    for conv, lab in zip(convergence_curves, labels):
        plt.plot(conv, marker='o', linestyle='-', linewidth=2, label=lab)
    plt.xlabel("Ітерація")
    plt.ylabel("Найкраще значення функції")
    plt.title(f"Порівняння експериментів: {description}")
    plt.legend()
    plt.grid(True)

    output_path = os.path.join(output_dir, f"comparison_{description.replace(' ', '_')}.png")
    plt.savefig(output_path)
    plt.close()
    print(f"Порівняльний графік збережено: {output_path}")


def compare_population_sizes(func, bounds, population_sizes, description, output_dir,
                             iterations=100,
                             w_max=0.9, w_min=0.4, c1=1.0, c2=2.5,
                             random_limits=None, break_faster=False, epsilon=1e-6, cnt_max=3,
                             clamp_velocity=1.0):
    
    #Порівнює різні розміри популяції для однієї функції.
    convergence_curves = []
    labels = []
    for pop_size in population_sizes:
        pso = PSO(
            func, bounds,
            swarm_size=pop_size,
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
        best_val, best_pos, conv_history, _ = pso.optimize()
        convergence_curves.append(conv_history)
        labels.append(f"pop_size={pop_size} (min={best_val:.6f})")

    plt.figure(figsize=(10,6))
    for conv, lab in zip(convergence_curves, labels):
        plt.plot(conv, marker='o', linestyle='-', linewidth=2, label=lab)
    plt.xlabel("Ітерація")
    plt.ylabel("Найкраще значення функції")
    plt.title(f"{description}")
    plt.legend()
    plt.grid(True)

    output_path = os.path.join(output_dir, f"population_comparison_{description.replace(' ', '_')}.png")
    plt.savefig(output_path)
    plt.close()
    print(f"Порівняльний графік збережено: {output_path}")


def compare_population_sizes_for_functions(functions, bounds_list, population_sizes_list, descriptions, output_dir,
                                           iterations=100,
                                           w_max=0.9, w_min=0.4, c1=1.0, c2=2.5,
                                           random_limits=None, break_faster=False, epsilon=1e-6, cnt_max=3,
                                           clamp_velocity=1.0):
    
    #Для кожної функції будує окремий графік, порівнюючи різні розміри популяції.

    for func, bounds, pop_sizes, desc in zip(functions, bounds_list, population_sizes_list, descriptions):
        compare_population_sizes(
            func=func,
            bounds=bounds,
            population_sizes=pop_sizes,
            description=desc,
            output_dir=output_dir,
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
