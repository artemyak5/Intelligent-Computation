from skfuzzy import control as ctrl

def adjust_time(base, temp_term):
    order = ['short', 'normal', 'long']
    idx = order.index(base)
    if temp_term == 'cold' and idx < len(order)-1:
        return order[idx+1]
    if temp_term == 'warm' and idx > 0:
        return order[idx-1]
    return base

def build_rules(ctrl_obj):
    rules = []

    # rice rules
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
    # default rice temperature and time
    rules.append(ctrl.Rule(ctrl_obj.dish['rice'], ctrl_obj.cook_temp['medium']))
    rules.append(ctrl.Rule(ctrl_obj.dish['rice'], ctrl_obj.cook_time['normal']))
    # Adjust rice cook_time for cold/warm start
    for temp in ['cold', 'warm']:
        adj = adjust_time('normal', temp)
        rules.append(ctrl.Rule(
            ctrl_obj.dish['rice'] & ctrl_obj.temp_in[temp],
            ctrl_obj.cook_time[adj]
        ))

    # soup rules
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
    rules.append(ctrl.Rule(ctrl_obj.dish['soup'], ctrl_obj.cook_time['normal']))

    # porridge rules
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
    rules.append(ctrl.Rule(ctrl_obj.dish['porridge'], ctrl_obj.cook_temp['medium']))
    rules.append(ctrl.Rule(ctrl_obj.dish['porridge'], ctrl_obj.cook_time['normal']))

    # stew rules
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
    rules.append(ctrl.Rule(ctrl_obj.dish['stew'], ctrl_obj.cook_temp['medium']))
    rules.append(ctrl.Rule(ctrl_obj.dish['stew'], ctrl_obj.cook_time['normal']))

    # steam rules
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

    # keep_warm rules
    rules.append(ctrl.Rule(
        ctrl_obj.dish['keep_warm'],
        ctrl_obj.cook_temp['low']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['keep_warm'],
        ctrl_obj.cook_time['short']
    ))

    # bake rules
    rules.append(ctrl.Rule(
        ctrl_obj.dish['bake'],
        ctrl_obj.cook_temp['high']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['bake'],
        ctrl_obj.cook_time['normal']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['bake'] & ctrl_obj.volume['large'],
        ctrl_obj.cook_time['long']
    ))

    # yogurt rules
    rules.append(ctrl.Rule(
        ctrl_obj.dish['yogurt'],
        ctrl_obj.cook_temp['low']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['yogurt'],
        ctrl_obj.cook_time['normal']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['yogurt'] & ctrl_obj.temp_in['cold'],
        ctrl_obj.cook_time['long']
    ))

    # reheat rules
    rules.append(ctrl.Rule(
        ctrl_obj.dish['reheat'],
        ctrl_obj.cook_temp['medium']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['reheat'],
        ctrl_obj.cook_time['normal']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['reheat'] & ctrl_obj.temp_in['warm'],
        ctrl_obj.cook_time['short']
    ))

    # sterilization rules
    rules.append(ctrl.Rule(
        ctrl_obj.dish['sterilization'],
        ctrl_obj.cook_temp['medium']
    ))
    rules.append(ctrl.Rule(
        ctrl_obj.dish['sterilization'],
        ctrl_obj.cook_time['long']
    ))
    # Adjust sterilization cook_time for cold/warm start
    for temp in ['cold', 'warm']:
        adj = adjust_time('long', temp)
        rules.append(ctrl.Rule(
            ctrl_obj.dish['sterilization'] & ctrl_obj.temp_in[temp],
            ctrl_obj.cook_time[adj]
        ))

    return rules
