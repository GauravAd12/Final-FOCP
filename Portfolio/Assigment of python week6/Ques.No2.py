# 2 write and test a function that takes an integer as its parameter and returns the
# factors of that integer W. (A factor is an integer which can be multiplied by another to
# yield the original).


def find_factors(n):
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return factors

# Example:
print(find_factors(12))  # Output: [1, 2, 3, 4, 6, 12]
