from scipy.stats import chisquare
import numpy as np
from data import data

a = [item for sublist in data for item in sublist]

def chi_square_test(numbers):
    # Count observed frequencies using np.bincount and ensuring non-negative numbers
    observed_frequencies = np.bincount(numbers).astype(int)

    # Calculate expected frequencies based on actual range of numbers
    min_number = np.min(numbers)
    max_number = np.max(numbers)
    num_possible_values = max_number - min_number + 1
    expected_frequency = len(numbers) / num_possible_values

    # Create expected frequencies array, matching length of observed frequencies
    expected_frequencies = np.full(len(observed_frequencies), expected_frequency)

    # Perform Chi-Square Test
    chi2, p = chisquare(observed_frequencies, expected_frequencies)

    return chi2, p

# Example usage with non-negative numbers:
lottery_numbers = a
chi2, p = chi_square_test(lottery_numbers)

print("Chi-Square Statistic:", chi2)
print("p-value:", p)
if p < 0.05:
    print("The lottery numbers do not follow a uniform distribution (significant deviation).")
else:
    print("The lottery numbers follow a uniform distribution (no significant deviation).")
