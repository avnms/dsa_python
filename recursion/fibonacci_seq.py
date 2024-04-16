cache = [None] * 100


def fibonacci(n):
    # Define the base case
    if n <= 1:
        return n

    # Check if the value exists in cache
    if not cache[n]:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache[n]


if __name__ == "__main__":
    print(fibonacci(6))
