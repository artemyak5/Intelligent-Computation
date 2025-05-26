from skfuzzy import control as ctrl
import skfuzzy as fuzz
import config

def define_volume_mfs(volume: ctrl.Antecedent):
    for name, params in config.VOLUME_MF.items():
        if len(params) == 3:
            volume[name] = fuzz.trimf(volume.universe, params)
        else:
            volume[name] = fuzz.trapmf(volume.universe, params)

def define_ratio_mfs(ratio: ctrl.Antecedent):
    for name, params in config.RATIO_MF.items():
        if len(params) == 3:
            ratio[name] = fuzz.trimf(ratio.universe, params)
        else:
            ratio[name] = fuzz.trapmf(ratio.universe, params)

def define_temp_in_mfs(temp_in: ctrl.Antecedent):
    for name, params in config.TEMP_IN_MF.items():
        if len(params) == 3:
            temp_in[name] = fuzz.trimf(temp_in.universe, params)
        else:
            temp_in[name] = fuzz.trapmf(temp_in.universe, params)

def define_cook_time_mfs(cook_time: ctrl.Consequent):
    for name, params in config.COOK_TIME_MF.items():
        if len(params) == 3:
            cook_time[name] = fuzz.trimf(cook_time.universe, params)
        else:
            cook_time[name] = fuzz.trapmf(cook_time.universe, params)

def define_cook_temp_mfs(cook_temp: ctrl.Consequent):
    for name, params in config.COOK_TEMP_MF.items():
        cook_temp[name] = fuzz.trimf(cook_temp.universe, params)
