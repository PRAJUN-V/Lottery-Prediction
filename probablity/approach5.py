from data1 import unflattened_list, unique_total_data, full_number
dictionary = {}

for i in unique_total_data:
    if unflattened_list.count(i) == 6:
        dictionary[i] = unflattened_list.count(i)


print(dictionary)
print(len(dictionary))