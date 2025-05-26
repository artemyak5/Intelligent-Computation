# Diapasons and MF parameters for fuzzy variables

# volume (0–5 L): small up to 2 L, medium around 2.5 L, large above 3 L
VOLUME_UNIVERSE = (0.0, 5.0)
VOLUME_MF = {
    'small':  [0, 0, 1, 2],    # trapmf
    'medium': [1, 2.5, 4],     # trimf
    'large':  [3, 4, 5, 5],    # trapmf
}

# ratio (1–3): low below 2, medium around 2, high above 2.5
RATIO_UNIVERSE = (1.0, 3.0)
RATIO_MF = {
    'low':    [1, 1, 1.5, 2],  # trapmf
    'medium': [1.5, 2, 2.5],   # trimf
    'high':   [2, 2.5, 3, 3],   # trapmf
}

# temp_in (0–30 °C): cold up to 15, moderate around 15, warm from 20
TEMP_IN_UNIVERSE = (0.0, 30.0)
TEMP_IN_MF = {
    'cold':     [0, 0, 10, 15],  # trapmf
    'moderate': [10, 15, 20],    # trimf
    'warm':     [15, 20, 30, 30],# trapmf
}

# cook_time (0–120 min): short up to 40, normal around 60, long above 80
COOK_TIME_UNIVERSE = (0.0, 120.0)
COOK_TIME_MF = {
    'short':  [0, 0, 20, 40],     # trapmf
    'normal': [30, 60, 90],       # trimf
    'long':   [80, 100, 120, 120],# trapmf
}

# cook_temp (35–180 °C): low around 50, medium around 90, high around 150
COOK_TEMP_UNIVERSE = (35.0, 180.0)
COOK_TEMP_MF = {
    'low':    [35, 50, 65],       # trimf
    'medium': [60, 90, 120],      # trimf
    'high':   [115, 150, 180],    # trimf
}
