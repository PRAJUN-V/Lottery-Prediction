import statistics
from data import data
# Example list of integers
numbers = data[26]

# Calculate the average using statistics.mean() and convert it to an integer
average = int(statistics.mean(numbers))
print("Average:", average)
