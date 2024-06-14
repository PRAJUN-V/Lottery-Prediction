from data1 import data,full_number

unflattened_list = [item for sublist in data for item in sublist]
unique_total_data = set(unflattened_list)

print(len(data))
print(len(unflattened_list))
print(len(unique_total_data))
print(len(unflattened_list) - len(unique_total_data))
print(len(full_number) - len(unique_total_data))
