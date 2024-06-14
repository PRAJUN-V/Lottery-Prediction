from data import data
a = [item for sublist in data for item in sublist]
from scipy.stats import kstest

def kolmogorov_smirnov_test(numbers):
    # Perform the Kolmogorov-Smirnov Test
    result = kstest(numbers, 'uniform')
    
    print("Kolmogorov-Smirnov Test Statistics:", result.statistic)
    print("p-value:", result.pvalue)
    if result.pvalue < 0.05:
        print("The sequence of lottery numbers does not appear to be random (significant deviation).")
    else:
        print("The sequence of lottery numbers appears to be random (no significant deviation).")

# Example usage:
kolmogorov_smirnov_test(a)
