X_values = [int(el) for el in '-1 1 3'.split()]
N_counts = [int(el) for el in '3 6 1'.split()]

def math_expectation(X:list, N:list):
    sample_size_N = sum(N_counts)
    return sum([X[i] * N[i] for i in range(len(N_counts))]) / sample_size_N

def variance(X:list, N:list):
    sample_size_N = sum(N_counts)
    return sum([X[i]**2 * N[i] for i in range(len(N_counts))]) / sample_size_N - math_expectation(X, N)**2

def standard_deviation(X:list, N:list):
    return variance(X, N) ** 0.5

def corrected_variance(X:list, N:list):
    sample_size_N = sum(N_counts)
    return variance(X, N) * sample_size_N / (sample_size_N - 1)

print('----------------')
for el in X_values:
    print("|{:3.0f} ".format(el), end='')
print('|\n----------------')

for el in N_counts:
    print("|{:3.0f} ".format(el), end='')
print('|\n----------------')

print("Math expectation M(X) =", math_expectation(X_values, N_counts))
print("Variance (Dispersion) D(X) =", round(variance(X_values, N_counts), 2))
print("Standard deviation sigma(X) =", round(standard_deviation(X_values, N_counts), 2))
print("Corrected variance S**2(X) =", round(corrected_variance(X_values, N_counts), 2))
print("Corrected standard deviation S(X) =", round(corrected_variance(X_values, N_counts)**0.5, 2))
