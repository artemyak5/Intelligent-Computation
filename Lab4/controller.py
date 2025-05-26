import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import config
from membership import (
    define_volume_mfs,
    define_ratio_mfs,
    define_temp_in_mfs,
    define_cook_time_mfs,
    define_cook_temp_mfs,
)
from rules import build_rules

class MulticookerController:
    def __init__(self):
        # Ініціалізація вхідних змінних
        self.volume = ctrl.Antecedent(np.arange(*config.VOLUME_UNIVERSE, 0.1), 'volume')
        self.ratio  = ctrl.Antecedent(np.arange(*config.RATIO_UNIVERSE,  0.01), 'ratio')
        self.temp_in= ctrl.Antecedent(np.arange(*config.TEMP_IN_UNIVERSE, 0.1), 'temp_in')
        self.dish   = ctrl.Antecedent(np.arange(0, 10, 1), 'dish')  # crisp singleton

        # Ініціалізація виходів із centroid-дефазифікацією
        self.cook_time = ctrl.Consequent(np.arange(*config.COOK_TIME_UNIVERSE, 0.1), 'cook_time')
        self.cook_time.defuzzify_method = 'centroid'

        self.cook_temp = ctrl.Consequent(np.arange(*config.COOK_TEMP_UNIVERSE, 0.1), 'cook_temp')
        self.cook_temp.defuzzify_method = 'centroid'

        # Визначення MF
        define_volume_mfs(self.volume)
        define_ratio_mfs(self.ratio)
        define_temp_in_mfs(self.temp_in)
        labels = ['rice','soup','porridge','stew','steam','keep_warm','bake','yogurt','reheat','sterilization']
        for i, name in enumerate(labels):
            # crisp membership: 1 тільки в одній точці
            self.dish[name] = fuzz.trimf(self.dish.universe, [i, i, i])
        define_cook_time_mfs(self.cook_time)
        define_cook_temp_mfs(self.cook_temp)

        # Побудова системи та симулятора
        rules = build_rules(self)
        self.system = ctrl.ControlSystem(rules)
        self.sim    = ctrl.ControlSystemSimulation(self.system)

    def compute(self, volume, ratio, temp_in, dish_code):
        # Скидаємо попередній стан
        self.sim.reset()
        # Призначаємо вхідні значення
        self.sim.input['volume']  = volume
        self.sim.input['ratio']   = ratio
        self.sim.input['temp_in'] = temp_in
        self.sim.input['dish']    = dish_code
        # Запускаємо обчислення
        self.sim.compute()
        # Повертаємо обидва виходи
        return self.sim.output['cook_time'], self.sim.output['cook_temp']
