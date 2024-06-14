from data1 import unflattened_list, unique_total_data

# Initialize dictionaries to store the counts of each digit in each place
ones_place_counts = {str(i): 0 for i in range(10)}
tens_place_counts = {str(i): 0 for i in range(10)}
hundreds_place_counts = {str(i): 0 for i in range(10)}
thousands_place_counts = {str(i): 0 for i in range(10)}

# Iterate over each integer in unique_total_data
for i in unique_total_data:
    # Convert the integer to a string
    str_i = str(i)

    # Get the digits in each place, treating missing places as 0
    ones_place_digit = str_i[-1]
    tens_place_digit = str_i[-2] if len(str_i) > 1 else '0'
    hundreds_place_digit = str_i[-3] if len(str_i) > 2 else '0'
    thousands_place_digit = str_i[-4] if len(str_i) > 3 else '0'

    # Increment the count of each digit in the respective dictionary
    ones_place_counts[ones_place_digit] += 1
    tens_place_counts[tens_place_digit] += 1
    hundreds_place_counts[hundreds_place_digit] += 1
    thousands_place_counts[thousands_place_digit] += 1

# Print the counts for each place and each digit
print("Counts for Ones Place:")
for digit, count in ones_place_counts.items():
    print(f"Count of {digit}: {count}")

print("\nCounts for Tens Place:")
for digit, count in tens_place_counts.items():
    print(f"Count of {digit}: {count}")

print("\nCounts for Hundreds Place:")
for digit, count in hundreds_place_counts.items():
    print(f"Count of {digit}: {count}")

print("\nCounts for Thousands Place:")
for digit, count in thousands_place_counts.items():
    print(f"Count of {digit}: {count}")