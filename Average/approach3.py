# flat_list = [item for sublist in nested_list for item in sublist] # This will flatten a 2d list

from data import data
a = []
for i in range(0,8):
    for j in data[i]:
        a.append(j)

b = sum(a) // len(a)
print(b)