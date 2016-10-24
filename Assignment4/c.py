from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.supervised.trainers import BackpropTrainer
import numpy
import matplotlib.pyplot as plt

ds = SupervisedDataSet(1, 1)

print("\nCreating dataset:")
for i in range(1, 9):
    ds.addSample(i, i)

for inpt, target in ds:
    print(inpt, "->", target)


print("\nBuilding network.")
net = buildNetwork(1, 2, 1, bias=True, hiddenclass=TanhLayer)

print("\nTraining until convergence.")
trainer = BackpropTrainer(net, ds)
results = trainer.trainUntilConvergence(
    verbose=False, validationProportion=0.15, maxEpochs=8000, continueEpochs=100)
for result in results:
    print(result)

print("\nRunning activations:")
for j in range(-8, 0):
    output = net.activate([j])
    print(j, "->", numpy.round(output), "\t", output)
print()

for j in range(1, 9):
    output = net.activate([j])
    print(j, "->", numpy.round(output), "\t", output)
print()

y_list, x_list = [], []
for j in range(-150, 150):
        val = j/10
        output = net.activate([val])
        x_list.append(val)
        y_list.append(output)
        # print(val, "->", numpy.round(output,1), "\t", output)

plt.plot(x_list, y_list)
plt.axis([-10, 15, -10, 15])
plt.grid(True, which='both')
plt.show()
