import math
import numpy as np

f = np.genfromtxt("input.txt")
l1 = sorted(f[:,0])
l2 = sorted(f[:,1])

total = 0

for i, j in zip(l1, l2):
    total += abs(i-j)

print(total)

d = dict()

for i in l2:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

similarity = sum([d[j]*j if j in d.keys() else 0 for j in l1])

print(similarity)