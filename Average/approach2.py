import itertools
from data import data
import statistics


# Generate all permutations
permutations = list(itertools.permutations(range(0, 52), 2))
u = []
# Print the permutations
for perm in permutations:
    x, y = perm
    if x < y:
        avg = int(statistics.mean(data[y]))
        if avg in data[x]:
            u.append([x,y])
print(u)
