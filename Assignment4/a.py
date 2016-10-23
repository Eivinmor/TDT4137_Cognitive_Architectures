import random

number_of_weights = 2
learning_rate = 0.1


def generate_random_weights(range_min, range_max):
    random_weights = []
    for i in range(number_of_weights):
        random_weights.append(round(random.uniform(range_min, range_max), 1))
    return random_weights

weights_list = generate_random_weights(-0.5, 0.5)
threshold = 0.2
print("\nThreshold:", threshold)
print("Learning rate:", learning_rate, end="\n\n")
print("\033[1m")
print('{:<6}'.format("Epoch"),
      '{:<8}'.format("Inputs"),
      '{:<8}'.format("Desired"),
      '{:<16}'.format("InitWghts"),
      '{:<8}'.format("Result"),
      '{:<8}'.format("Actual"),
      '{:<8}'.format("Error"),
      '{:<16}'.format("FinalWghts"))
print("\033[0m", end="")


def perceptron(input_list, desired_output):

    print('{:<8}'.format(str(input_list)), end=" ")
    print('{:<8}'.format(desired_output), end=" ")
    round_weights = [round(weight, 2) for weight in weights_list]
    print('{:<16}'.format(str(round_weights)), end=" ")

    actual_output = step_activation(input_list)
    error = desired_output - actual_output
    for i in range(len(input_list)):
        update_weight(i, input_list[i], error)

    print('{:<8}'.format(actual_output), end=" ")
    print('{:<8}'.format(error), end=" ")
    round_weights = [round(weight, 2) for weight in weights_list]
    print('{:<16}'.format(str(round_weights)))

    return error


def step_activation(input_list):
    result = 0
    for i in range(number_of_weights):
        result += input_list[i] * weights_list[i]
    print('{:<8}'.format(round(result, 1)), end=" ")
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
    print('{:<6}'.format(epoch), end=" ")
    total_error += abs(perceptron([0, 0], 0))
    print('{:<6}'.format(""), end=" ")
    total_error += abs(perceptron([0, 1], 0))
    print('{:<6}'.format(""), end=" ")
    total_error += abs(perceptron([1, 0], 0))
    print('{:<6}'.format(""), end=" ")
    total_error += abs(perceptron([1, 1], 1))
    print()
