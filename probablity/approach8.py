from data import total_data
from data1 import data
a = total_data[-1]
b = sorted([item for sublist in data[0:len(data) - 1] for item in sublist])
c = []
for i in a:
    if i not in b:
        c.append(i)

print(len(c))
print(len(a))
print(c)