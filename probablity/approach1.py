# data, data1 etc are list
from data import data_1, data1, data2, data3

data_list = [data_1, data1, data2, data3]
data_set = []

for i in data_list:
    data_set.append(set(i))  
 
print(data_set[0] & data_set[1])
print(data_set[0] & data_set[2])
print(data_set[0] & data_set[3])
print(data_set[1] & data_set[2])
print(data_set[1] & data_set[3])
print(data_set[2] & data_set[3])
