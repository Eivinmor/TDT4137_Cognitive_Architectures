import random

number_of_weights = 2
learning_rate = 0.1


def generate_random_weights(range_min, range_max):
    random_weights = []
    for i in range(number_of_weights):
        random_weights.append(random.randint(range_min*10, range_max*10)/10)
    return random_weights

weights_list = generate_random_weights(-0.5, 0.5)
threshold = 0.2
print("\nThreshold:", threshold)
print("Learning rate:", learning_rate, end="\n\n")
print("\033[1m")
print('{:<5}'.format("Epoch"),
      '{:>8}'.format("Inputs"),
      '{:>8}'.format("Desired"),
      '{:>14}'.format("InitWghts"),
      '{:>10}'.format("Result"),
      '{:>8}'.format("Actual"),
      '{:>8}'.format("Error"),
      '{:>14}'.format("FinalWghts"),
      "\033[0m")


def perceptron(input_list, desired_output):
    print('{:>8}'.format(str(input_list)), end=" ")
    print('{:>8}'.format(desired_output), end=" ")
    print('{:>2}'.format(""), end=" ")
    for weight in weights_list: print("{:>5}".format("{0:.1f}".format(weight)), end=" ")

    actual_output = step_activation(input_list)
    error = desired_output - actual_output
    for i in range(len(input_list)):
        update_weight(i, input_list[i], error)

    print('{:>8}'.format(actual_output), end=" ")
    print('{:>8}'.format(error), end=" ")
    print('{:>2}'.format(""), end=" ")
    for weight in weights_list: print("{:>5}".format("{0:.1f}".format(weight)), end=" ")
    print()
    return error


def step_activation(input_list):
    result = 0
    for i in range(number_of_weights):
        result += input_list[i] * weights_list[i]
        result = round(result, 1)
    print('{:>10}'.format(result), end=" ")
    if result >= threshold:
        return 1
    return 0


def update_weight(index, input_value, error):
    weights_list[index] += learning_rate * input_value * error

total_error = 1
epoch = 0
while total_error != 0:
    total_error = 0
    epoch += 1
    print('{:<5}'.format(epoch), end=" ")
    total_error += abs(perceptron([0, 0], 0))
    print('{:<5}'.format(""), end=" ")
    total_error += abs(perceptron([0, 1], 0))
    print('{:<5}'.format(""), end=" ")
    total_error += abs(perceptron([1, 0], 0))
    print('{:<5}'.format(""), end=" ")
    total_error += abs(perceptron([1, 1], 1))
    print()
