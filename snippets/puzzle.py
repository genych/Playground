import itertools as it
import numpy as np

planks = ['02143230', '02352140', '03424520', '05241320']
slices = []

ident = ~np.identity(4, dtype=bool)
ident = ident.astype(int)

for plank in planks:
    tmp = []
    for x in range(5):
        tmp.append(plank[x: x + 4])
    slices.append(tmp)

permutations = it.permutations(slices, 4)

for item in permutations:
    cartesian = it.product(*item)

    for position in cartesian:
        matrix = np.array([[int(char) for char in list(slc)]
                            for slc in position])
        matrix *= ident
        vertical_sum = matrix.sum(axis=0)

        if (vertical_sum == 10).all():
            print matrix
