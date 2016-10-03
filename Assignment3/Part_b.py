import math

distance_dictionary = {
    "VerySmall": {"type": "reverse_grade", "x0": 1, "x1": 2.5},
    "Small": {"type": "triangle", "x0": 1.5, "x1": 3, "x2": 4.5},
    "Perfect": {"type": "triangle", "x0": 3.5, "x1": 5, "x2": 6.5},
    "Big": {"type": "triangle", "x0": 5.5, "x1": 7, "x2": 8.5},
    "VeryBig": {"type": "grade", "x0": 7.5, "x1": 9}
}

delta_dictionary = {
    "ShrinkingFast": {"type": "reverse_grade", "x0": -4, "x1": -2.5},
    "Shrinking": {"type": "triangle", "x0": -3.5, "x1": -2, "x2": -0.5},
    "Stable": {"type": "triangle", "x0": -1.5, "x1": 0, "x2": 1.5},
    "Growing": {"type": "triangle", "x0": 0.5, "x1": 2, "x2": 3.5},
    "GrowingFast": {"type": "grade", "x0": 2.5, "x1": 4},
}

def triangle(position, x0, x1, x2, clip):
    value = 0.0
    if position >= x0 and position <= x1:
            value = (position - x0) / (x1 - x0)
    elif position >= x1 and position <= x2:
            value = (x2 - position) / (x1 - x0)
    if value > clip:
            value = clip;
    return value

def grade(position, x0, x1, clip):
    value = 0.0
    if position >= x1:
        value = 1.0
    elif position <= x0:
        value = 0.0
    else:
        value = (position - x0) / (x1 - x0)
    if value > clip:
        value = clip
    return value


def reverse_grade(position, x0, x1, clip):
    value = 0.0
    if position <= x0: value = 1.0
    elif position >= x1:
        value = 0.0
    else:
        value = (x1 - position) / (x1 - x0)
    if value > clip:
        value = clip;
    return value
