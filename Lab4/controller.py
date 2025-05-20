import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from rules import build_rules

class MulticookerController:
    def __init__(self):
        # 1. Оголошуємо Antecedent і Consequent
        self.volume = ctrl.Antecedent(np.arange(0, 5.1, 0.1), 'volume')
        self.ratio = ctrl.Antecedent(np.arange(1, 3.01, 0.01), 'ratio')
        self.temp_in = ctrl.Antecedent(np.arange(0, 30.1, 0.1), 'temp_in')
        self.dish = ctrl.Antecedent(np.arange(0, 10, 1), 'dish')  # numeric codes: 0..9
        self.cook_time = ctrl.Consequent(np.arange(0, 120.1, 0.1), 'cook_time')
        self.cook_temp = ctrl.Consequent(np.arange(35, 180.1, 0.1), 'cook_temp')

        # 2. Будуємо функції приналежності
        self._define_mfs()

        # 3. Завантажуємо правила
        rules = build_rules(self)
        self.system = ctrl.ControlSystem(rules)
        self.sim = ctrl.ControlSystemSimulation(self.system)

    def _define_mfs(self):
        # volume
        self.volume['small']  = fuzz.trapmf(self.volume.universe, [0, 0, 1, 2])
        self.volume['medium'] = fuzz.trimf(self.volume.universe, [1, 2.5, 4])
        self.volume['large']  = fuzz.trapmf(self.volume.universe, [3, 4, 5, 5])
        # ratio
        self.ratio['low']    = fuzz.trapmf(self.ratio.universe, [1, 1, 1.5, 2])
        self.ratio['medium'] = fuzz.trimf(self.ratio.universe, [1.5, 2, 2.5])
        self.ratio['high']   = fuzz.trapmf(self.ratio.universe, [2, 2.5, 3, 3])
        # temp_in
        self.temp_in['cold']     = fuzz.trapmf(self.temp_in.universe, [0, 0, 10, 15])
        self.temp_in['moderate'] = fuzz.trimf(self.temp_in.universe, [10, 15, 20])
        self.temp_in['warm']     = fuzz.trapmf(self.temp_in.universe, [15, 20, 30, 30])
        # dish types
        labels = ['rice', 'soup', 'porridge', 'stew', 'steam', 'keep_warm', 'bake', 'yogurt', 'reheat', 'sterilization']
        for i, name in enumerate(labels):
            self.dish[name] = fuzz.trimf(self.dish.universe, [i-0.5, i, i+0.5])
        # cook_time
        self.cook_time['short']  = fuzz.trapmf(self.cook_time.universe, [0, 0, 20, 40])
        self.cook_time['normal'] = fuzz.trimf(self.cook_time.universe, [30, 60, 90])
        self.cook_time['long']   = fuzz.trapmf(self.cook_time.universe, [80, 100, 120, 120])
        # cook_temp
        self.cook_temp['low']    = fuzz.trimf(self.cook_temp.universe, [35, 50, 65])
        self.cook_temp['medium'] = fuzz.trimf(self.cook_temp.universe, [60, 90, 120])
        self.cook_temp['high']   = fuzz.trimf(self.cook_temp.universe, [115, 150, 180])

    def compute(self, volume, ratio, temp_in, dish_code):
        self.sim.input['volume'] = volume
        self.sim.input['ratio']  = ratio
        self.sim.input['temp_in']= temp_in
        # Set numeric code for dish
        self.sim.input['dish']   = dish_code
        self.sim.compute()
        return self.sim.output['cook_time'], self.sim.output['cook_temp']