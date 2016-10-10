import sys
this_module = sys.modules[__name__]

distance_dict = {
    "VerySmall": {"type": "reverse_grade", "x": [1, 2.5]},
    "Small": {"type": "triangle", "x": [1.5, 3, 4.5]},
    "Perfect": {"type": "triangle", "x": [3.5, 5, 6.5]},
    "Big": {"type": "triangle", "x": [5.5, 7, 8.5]},
    "VeryBig": {"type": "grade", "x": [7.5, 9]}
}

delta_dict = {
    "ShrinkingFast": {"type": "reverse_grade", "x": [-4, -2.5]},
    "Shrinking": {"type": "triangle", "x": [-3.5, -2, -0.5]},
    "Stable": {"type": "triangle", "x": [-1.5, 0, 1.5]},
    "Growing": {"type": "triangle", "x": [0.5, 2, 3.5]},
    "GrowingFast": {"type": "grade", "x": [2.5, 4]},
}

action_dict = {
    "BrakeHard": {"type": "reverse_grade", "x": [-8, -5], "cut": 1.0},
    "SlowDown": {"type": "triangle", "x": [-7, -4, -1],  "cut": 1.0},
    "None": {"type": "triangle", "x": [-3, 0, 3],  "cut": 1.0},
    "SpeedUp": {"type": "triangle", "x": [1, 4, 7],  "cut": 1.0},
    "FloorIt": {"type": "grade", "x": [5, 8],  "cut": 1.0},
}

distance_value = 3.7
delta_value = 1.2

action_range_min = -10
action_range_max = 10


def mamdani_resonate():
    action_dict["None"]["cut"] = AND(fuzzy("Small"), fuzzy("Growing"))
    action_dict["SlowDown"]["cut"] = AND(fuzzy("Small"), fuzzy("Stable"))
    action_dict["SpeedUp"]["cut"] = AND(fuzzy("Perfect"), fuzzy("Growing"))
    action_dict["FloorIt"]["cut"] = AND(fuzzy("VeryBig"), OR(NOT(fuzzy("Growing")), NOT(fuzzy("GrowingFast"))))
    action_dict["BrakeHard"]["cut"] = fuzzy("VerySmall")

    print("\nCut values:")
    for key, dict in action_dict.items():
        print("{:<12}".format(key), round(dict["cut"], 2))
    print("\n")

    dividend = 0
    divisor = 0
    for position in range(action_range_min, action_range_max + 1):
        max_action, max_value = get_max_action(position)
        dividend += position * max_value
        divisor += max_value
        print("{:>3}".format(position), "  ", end="")
        print("{:<8}".format(max_action), "   ", end="")
        print("{:<6}".format(round(max_value, 2)), end="\t")
        i = 0
        while i < max_value*30:
            print("-", end="")
            i += 1
        print("*")

    cog = dividend/divisor
    print("\nCOG: ", cog)
    cog_action, cog_value = get_max_action(cog)
    print("Action: ", cog_action)


def get_max_action(position):
    cur_max_action = "-"
    cur_max_value = 0
    for key in action_dict.keys():
        value = get_value(key, position)
        if value > cur_max_value:
            cur_max_action = key
            cur_max_value = value
    return cur_max_action, cur_max_value

def fuzzy(var):
    if var in distance_dict:
        position = distance_value
        var_dict = distance_dict[var]
    elif var in delta_dict:
        position = delta_value
        var_dict = delta_dict[var]
    function = getattr(this_module, var_dict["type"])
    fuzzy_value = function(position, var_dict["x"], 1)
    return fuzzy_value

def get_value(action, position):
    function = getattr(this_module, action_dict[action]["type"])
    value = function(position, action_dict[action]["x"], action_dict[action]["cut"])
    return value


def AND(a, b):
    return min(a, b)


def OR(a, b):
    return max(a, b)


def NOT(a):
    return 1-a


def triangle(position, x, cut):
    value = 0.0
    if position >= x[0] and position <= x[1]:
            value = (position - x[0]) / (x[1] - x[0])
    elif position >= x[1] and position <= x[2]:
            value = (x[2] - position) / (x[1] - x[0])
    if value > cut:
            value = cut
    return value


def grade(position, x, cut):
    value = 0.0
    if position >= x[1]:
        value = 1.0
    elif position <= x[0]:
        value = 0.0
    else:
        value = (position - x[0]) / (x[1] - x[0])
    if value > cut:
        value = cut
    return value


def reverse_grade(position, x, cut):
    value = 0.0
    if position <= x[0]: value = 1.0
    elif position >= x[1]:
        value = 0.0
    else:
        value = (x[1] - position) / (x[1] - x[0])
    if value > cut:
        value = cut
    return value


mamdani_resonate()
