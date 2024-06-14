from data1 import unflattened_list, unique_total_data, full_number , unlotted
import random

# randomly picking a number from unlotted code
l = len(unlotted)
prediction_list = []
for i in range(10):
    r = random.randint(0, l)
    a = unlotted[r]
    prediction_list.append(a)
print(prediction_list)
