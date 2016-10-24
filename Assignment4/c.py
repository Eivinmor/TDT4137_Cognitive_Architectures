from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.supervised.trainers import BackpropTrainer
import numpy

ds = SupervisedDataSet(1, 1)

print("\nCreating dataset:")
ds.addSample(1, 1)
ds.addSample(2, 2)
ds.addSample(3, 3)
ds.addSample(4, 4)
ds.addSample(5, 5)
ds.addSample(6, 6)
ds.addSample(7, 7)
ds.addSample(8, 8)

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
for j in range(1, 9):
    output = net.activate([j])
    print(j, "->", numpy.round(output), "\t", output)
