import random

number_of_weights = 2
weights_list = []
learning_rate = 0.05


def generate_random_weights(range_min, range_max):
    for i in range(number_of_weights):
        weights_list.append(random.uniform(range_min, range_max))

generate_random_weights(-0.5, 0.5)
threshold = random.uniform(-0.5, 0.5)
print("Threshold:", threshold, end="\n\n")


def perceptron(input_list, desired_output):
    actual_output = neuron_sign(input_list)
    error = desired_output - actual_output
    print("Input:", input_list)
    print("Weights:", weights_list)
    print("Desired output:", desired_output)
    print("Actual output", actual_output)
    print("Error:", error)
    for i in range(len(weights_list)):
        update_weight(i, input_list[i], error)
    print("New weights:", weights_list)


def neuron_sign(input_list):
    result = 0
    for i in range(len(input_list)):
        result += input_list[i]*weights_list[i] -  threshold
    if result >= 0:
        return 1
    return 0


def update_weight(index, input_value, error):
    print("Input" + str(index) + ":", input_value)
    weights_list[index] += learning_rate * input_value * error

for i in range(3000):
    perceptron([0, 0], 0)
    print()
    perceptron([0, 1], 0)
    print()
    perceptron([1, 0], 0)
    print()
    perceptron([1, 1], 1)
    print()
    print("--------------------------------------------")
