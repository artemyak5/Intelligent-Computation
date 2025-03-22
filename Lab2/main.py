import os
import numpy as np
from results import run_experiment
from experiments import compare_experiments, compare_population_sizes_for_functions

output_dir = "result"
os.makedirs(output_dir, exist_ok=True)

def ackley(x):
    a, b, c = 20, 0.2, 2 * np.pi
    d = len(x)
    return -a * np.exp(-b * np.sqrt(np.sum(x**2)/d)) - np.exp(np.sum(np.cos(c * x))/d) + a + np.exp(1)

def rosenbrock(x):
    return (1 - x[0])**2 + 100*(x[1] - x[0]**2)**2

def cross_in_tray(x):
    term = np.abs(np.sin(x[0])*np.sin(x[1])*np.exp(np.abs(100 - np.sqrt(x[0]**2 + x[1]**2)/np.pi)))
    return -0.0001 * (term + 1)**0.1

def holder_table(x):
    return -np.abs(np.sin(x[0])*np.cos(x[1])*np.exp(np.abs(1 - np.sqrt(x[0]**2 + x[1]**2)/np.pi)))

def mccormick(x):
    return np.sin(x[0]+x[1]) + (x[0]-x[1])**2 - 1.5*x[0] + 2.5*x[1] + 1

def styblinski_tang(x):
    return 0.5 * np.sum(x**4 - 16*x**2 + 5*x)

# --- Області пошуку ---
bounds_ackley = np.array([[-5, 5], [-5, 5]])
bounds_rosenbrock = np.array([[-2, 2], [-1, 3]])
bounds_cross = np.array([[-10, 10], [-10, 10]])
bounds_holder = np.array([[-10, 10], [-10, 10]])
bounds_mccormick = np.array([[-1.5, 4], [-3, 4]])
bounds_styblinski = np.array([[-5, 5], [-5, 5]])


iterations = 100
w_max = 0.9   # початкове w
w_min = 0.4   # кінцеве w (щоб до кінця ітерацій рій сильно "стиснувся")
c1 = 1.0      # помірний когнітивний вплив
c2 = 2.5      # посилений соціальний вплив
clamp_velocity = 1.0  
random_limits = None  


run_experiment(
    ackley, bounds_ackley, 0, "Ackley Function", output_dir,
    swarm_size=50, iterations=iterations,
    w_max=w_max, w_min=w_min,
    c1=c1, c2=c2,
    random_limits=random_limits,
    break_faster=False, epsilon=1e-6, cnt_max=3,
    clamp_velocity=clamp_velocity
)
run_experiment(
    rosenbrock, bounds_rosenbrock, 0, "Rosenbrock Function", output_dir,
    swarm_size=50, iterations=iterations,
    w_max=w_max, w_min=w_min,
    c1=c1, c2=c2,
    random_limits=random_limits,
    break_faster=False, epsilon=1e-6, cnt_max=3,
    clamp_velocity=clamp_velocity
)
run_experiment(
    cross_in_tray, bounds_cross, -2.06261, "Cross-In-Tray Function", output_dir,
    swarm_size=50, iterations=iterations,
    w_max=w_max, w_min=w_min,
    c1=c1, c2=c2,
    random_limits=random_limits,
    break_faster=False, epsilon=1e-6, cnt_max=3,
    clamp_velocity=clamp_velocity
)
run_experiment(
    holder_table, bounds_holder, -19.2085, "Holder Table Function", output_dir,
    swarm_size=50, iterations=iterations,
    w_max=w_max, w_min=w_min,
    c1=c1, c2=c2,
    random_limits=random_limits,
    break_faster=False, epsilon=1e-6, cnt_max=3,
    clamp_velocity=clamp_velocity
)
run_experiment(
    mccormick, bounds_mccormick, -1.9133, "McCormick Function", output_dir,
    swarm_size=50, iterations=iterations,
    w_max=w_max, w_min=w_min,
    c1=c1, c2=c2,
    random_limits=random_limits,
    break_faster=False, epsilon=1e-6, cnt_max=3,
    clamp_velocity=clamp_velocity
)
run_experiment(
    styblinski_tang, bounds_styblinski, -78.332, "Styblinski–Tang Function", output_dir,
    swarm_size=50, iterations=iterations,
    w_max=w_max, w_min=w_min,
    c1=c1, c2=c2,
    random_limits=random_limits,
    break_faster=False, epsilon=1e-6, cnt_max=3,
    clamp_velocity=clamp_velocity
)

# --- Порівняльний аналіз для функції Ackley з різними гіперпараметрами ---
exp_params = [
    {
        'swarm_size': 50, 'iterations': iterations,
        'w_max': 0.9, 'w_min': 0.4, 'c1': 1.0, 'c2': 2.5,
        'label': 'Стандарт (сильний соціальний)'
    },
    {
        'swarm_size': 50, 'iterations': iterations,
        'w_max': 0.9, 'w_min': 0.5, 'c1': 1.5, 'c2': 2.0,
        'label': 'Трохи інший варіант'
    }
]
compare_experiments(
    ackley, bounds_ackley, exp_params, "Ackley Function", output_dir,
    random_limits=random_limits, break_faster=False, epsilon=1e-6, cnt_max=3,
    clamp_velocity=clamp_velocity
)

# --- Порівняння різних розмірів популяції для кожної функції ---
function_list = [
    ackley, rosenbrock, cross_in_tray,
    holder_table, mccormick, styblinski_tang
]
bounds_list = [
    bounds_ackley, bounds_rosenbrock, bounds_cross,
    bounds_holder, bounds_mccormick, bounds_styblinski
]
descriptions = [
    "Ackley Function",
    "Rosenbrock Function",
    "Cross-In-Tray Function",
    "Holder Table Function",
    "McCormick Function",
    "Styblinski–Tang Function"
]
common_pop_sizes = [20, 50, 100, 250]
population_sizes_list = [common_pop_sizes] * len(function_list)

compare_population_sizes_for_functions(
    functions=function_list,
    bounds_list=bounds_list,
    population_sizes_list=population_sizes_list,
    descriptions=descriptions,
    output_dir=output_dir,
    iterations=iterations,
    w_max=w_max, w_min=w_min,
    c1=c1, c2=c2,
    random_limits=random_limits,
    break_faster=False, epsilon=1e-6, cnt_max=3,
    clamp_velocity=clamp_velocity
)
