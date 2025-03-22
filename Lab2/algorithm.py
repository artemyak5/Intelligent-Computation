import numpy as np

class Particle:
    def __init__(self, dim, bounds):
        # Початкова позиція в межах області пошуку
        self.position = np.random.uniform(bounds[:, 0], bounds[:, 1], dim)
        # Початкова швидкість
        self.velocity = np.random.uniform(-1, 1, dim)
        self.best_position = self.position.copy()
        self.best_value = float('inf')


class PSO:
    def __init__(self, func, bounds, swarm_size=50, iterations=100,
                 w_max=0.9, w_min=0.4,
                 c1=1.0, c2=2.5,  # посилений соціальний коеф.
                 random_limits=None,
                 break_faster=False, epsilon=1e-6, cnt_max=3,
                 clamp_velocity=1.0):
        """
        Параметри:
          func          : цільова функція
          bounds        : межі пошуку (масив розміром (dim, 2))
          swarm_size    : кількість частинок
          iterations    : максимальна кількість ітерацій
          w_max, w_min  : максимальна та мінімальна інерційні ваги (лінійне зменшення)
          c1, c2        : когнітивний та соціальний коефіцієнти
          random_limits : кортеж (low, high) для випадкових коеф. (a1, a2), якщо задано
          break_faster  : якщо True, алгоритм завершується достроково при відсутності покращення
          epsilon       : поріг для перевірки відсутності покращення
          cnt_max       : кількість ітерацій без покращення для дострокового завершення
          clamp_velocity: якщо не None, обмеження максимальної швидкості (+/- clamp_velocity)
        """
        self.func = func
        self.bounds = bounds
        self.dim = bounds.shape[0]
        self.swarm_size = swarm_size
        self.iterations = iterations

        self.w_max = w_max
        self.w_min = w_min
        self.c1 = c1
        self.c2 = c2
        self.random_limits = random_limits
        self.break_faster = break_faster
        self.epsilon = epsilon
        self.cnt_max = cnt_max
        self.clamp_velocity = clamp_velocity

        # Ініціалізація рою
        self.swarm = [Particle(self.dim, self.bounds) for _ in range(self.swarm_size)]
        self.global_best_val = float('inf')
        self.global_best_pos = None
        self.pos_history = []    # Історія положень частинок за ітераціями
        self.conv_history = []   # Історія глобально найкращих значень функції

        self.same_count = 0
        self.last_global_best = float('inf')

    def optimize(self):
        for it in range(self.iterations):
            iter_positions = []
            # Оцінка цільової функції для кожної частинки
            for particle in self.swarm:
                fitness = self.func(particle.position)
                # Оновлення персонального рекорду
                if fitness < particle.best_value:
                    particle.best_value = fitness
                    particle.best_position = particle.position.copy()
                # Оновлення глобального рекорду
                if fitness < self.global_best_val:
                    self.global_best_val = fitness
                    self.global_best_pos = particle.position.copy()
                iter_positions.append(particle.position.copy())

            self.pos_history.append(iter_positions)
            self.conv_history.append(self.global_best_val)

            # Перевірка умови дострокового завершення
            if abs(self.last_global_best - self.global_best_val) < self.epsilon:
                self.same_count += 1
            else:
                self.same_count = 0
            self.last_global_best = self.global_best_val
            if self.break_faster and self.same_count >= self.cnt_max:
                print(f"Дострокове завершення на ітерації {it+1} (без зміни значення)")
                break

            # Лінійне зменшення інерційної ваги (від w_max до w_min)
            w_current = self.w_max - (self.w_max - self.w_min) * (it / (self.iterations - 1))

            # Оновлення швидкостей і позицій частинок
            for particle in self.swarm:
                r1 = np.random.rand(self.dim)
                r2 = np.random.rand(self.dim)
                # Якщо задано random_limits – генеруємо коефіцієнти a1, a2 випадково
                if self.random_limits is not None:
                    low, high = self.random_limits
                    a1 = np.random.uniform(low, high, self.dim)
                    a2 = np.random.uniform(low, high, self.dim)
                    cognitive = a1 * r1 * (particle.best_position - particle.position)
                    social = a2 * r2 * (self.global_best_pos - particle.position)
                else:
                    cognitive = self.c1 * r1 * (particle.best_position - particle.position)
                    social = self.c2 * r2 * (self.global_best_pos - particle.position)

                particle.velocity = w_current * particle.velocity + cognitive + social

                # Обмеження максимальної швидкості
                if self.clamp_velocity is not None:
                    particle.velocity = np.clip(particle.velocity, -self.clamp_velocity, self.clamp_velocity)

                # Оновлюємо позицію
                particle.position += particle.velocity

                # «Відбивання» від меж
                for d in range(self.dim):
                    if particle.position[d] > self.bounds[d, 1]:
                        particle.position[d] = self.bounds[d, 1] - abs(particle.position[d] - self.bounds[d, 1])
                        particle.velocity[d] = -particle.velocity[d]
                    elif particle.position[d] < self.bounds[d, 0]:
                        particle.position[d] = self.bounds[d, 0] + abs(particle.position[d] - self.bounds[d, 0])
                        particle.velocity[d] = -particle.velocity[d]

        return self.global_best_val, self.global_best_pos, self.conv_history, self.pos_history
