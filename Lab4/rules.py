from skfuzzy import control as ctrl
import skfuzzy as fuzz

def build_rules(ctrl_obj):
    rules = []

    # Режим rice
    rules.append(ctrl.Rule(
        ctrl_obj.dish['rice'] & ctrl_obj.volume['small'] & ctrl_obj.ratio['low'],
        ctrl_obj.cook_time['short']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['rice'] & ctrl_obj.volume['medium'] & ctrl_obj.ratio['medium'],
        ctrl_obj.cook_time['normal']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['rice'] & ctrl_obj.volume['large'] & ctrl_obj.ratio['high'],
        ctrl_obj.cook_time['long']
    ))
    # Default cook_temp for rice
    rules.append(ctrl.Rule(
        ctrl_obj.dish['rice'],
        ctrl_obj.cook_temp['medium']
    ))

    # Режим soup
    rules.append(ctrl.Rule(
        ctrl_obj.dish['soup'] & ctrl_obj.volume['small'],
        ctrl_obj.cook_time['short']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['soup'] & ctrl_obj.volume['large'],
        ctrl_obj.cook_time['long']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['soup'] & ctrl_obj.temp_in['cold'],
        ctrl_obj.cook_time['long']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['soup'] & ctrl_obj.ratio['high'],
        ctrl_obj.cook_temp['medium']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['soup'] & ctrl_obj.ratio['low'],
        ctrl_obj.cook_temp['high']
    ))

    # Режим porridge
    rules.append(ctrl.Rule(
        ctrl_obj.dish['porridge'] & ctrl_obj.ratio['medium'],
        ctrl_obj.cook_time['normal']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['porridge'] & ctrl_obj.ratio['high'],
        ctrl_obj.cook_time['long']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['porridge'] & ctrl_obj.temp_in['warm'],
        ctrl_obj.cook_time['short']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['porridge'] & ctrl_obj.temp_in['cold'],
        ctrl_obj.cook_time['long']
    ))
    # Default cook_temp for porridge
    rules.append(ctrl.Rule(
        ctrl_obj.dish['porridge'],
        ctrl_obj.cook_temp['medium']
    ))

    # Режим stew
    rules.append(ctrl.Rule(
        ctrl_obj.dish['stew'] & ctrl_obj.volume['large'],
        ctrl_obj.cook_time['long']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['stew'] & ctrl_obj.ratio['medium'],
        ctrl_obj.cook_time['normal']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['stew'] & ctrl_obj.temp_in['cold'],
        ctrl_obj.cook_time['long']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['stew'] & ctrl_obj.temp_in['warm'],
        ctrl_obj.cook_time['normal']
    ))
    # Default cook_temp for stew
    rules.append(ctrl.Rule(
        ctrl_obj.dish['stew'],
        ctrl_obj.cook_temp['medium']
    ))

    # Режим steam
    rules.append(ctrl.Rule(
        ctrl_obj.dish['steam'],
        ctrl_obj.cook_temp['high']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['steam'] & ctrl_obj.volume['small'],
        ctrl_obj.cook_time['short']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['steam'] & ctrl_obj.volume['large'],
        ctrl_obj.cook_time['normal']
    ))

    # Режим keep_warm
    rules.append(ctrl.Rule(
        ctrl_obj.dish['keep_warm'],
        ctrl_obj.cook_temp['low']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['keep_warm'],
        ctrl_obj.cook_time['short']
    ))

    # Режим bake
    rules.append(ctrl.Rule(
        ctrl_obj.dish['bake'],
        ctrl_obj.cook_temp['high']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['bake'] & ctrl_obj.volume['small'],
        ctrl_obj.cook_time['normal']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['bake'] & ctrl_obj.volume['large'],
        ctrl_obj.cook_time['long']
    ))

    # Режим yogurt
    rules.append(ctrl.Rule(
        ctrl_obj.dish['yogurt'],
        ctrl_obj.cook_temp['low']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['yogurt'] & ctrl_obj.temp_in['warm'],
        ctrl_obj.cook_time['normal']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['yogurt'] & ctrl_obj.temp_in['cold'],
        ctrl_obj.cook_time['long']
    ))

    # Режим reheat
    rules.append(ctrl.Rule(
        ctrl_obj.dish['reheat'],
        ctrl_obj.cook_temp['medium']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['reheat'] & ctrl_obj.temp_in['cold'],
        ctrl_obj.cook_time['normal']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['reheat'] & ctrl_obj.temp_in['warm'],
        ctrl_obj.cook_time['short']
    ))

    # Режим sterilization
    rules.append(ctrl.Rule(
        ctrl_obj.dish['sterilization'],
        ctrl_obj.cook_temp['medium']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['sterilization'],
        ctrl_obj.cook_time['long']
    ))

        # Default cook_time for static modes bake, yogurt, reheat
    rules.append(ctrl.Rule(
        ctrl_obj.dish['bake'],
        ctrl_obj.cook_time['normal']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['yogurt'],
        ctrl_obj.cook_time['normal']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['reheat'],
        ctrl_obj.cook_time['normal']
    ))

    return rules