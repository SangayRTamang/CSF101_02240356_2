def fibonacci_iterative_list(n):
    """Returns a list of Fibonacci numbers up to F(n)."""
    if n <= 0:
        return [0]
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

n = 10
print(f"Fibonacci list up to F({n}): {fibonacci_iterative_list(n)}")


def first_fib_exceeding(value):
    """Finds the index of the first Fibonacci number that exceeds a given value."""
    a, b = 0, 1
    index = 0
    while a <= value:
        a, b = b, a + b
        index += 1
    return index, a

value = 50
index, fib_value = first_fib_exceeding(value)
print(f"The first Fibonacci number exceeding {value} is F({index}) = {fib_value}")


def is_fibonacci(number):
    """Checks if a given number is a Fibonacci number."""
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
    return a == number

test_number = 21
print(f"Is {test_number} a Fibonacci number? {is_fibonacci(test_number)}")


def fibonacci_ratios(limit):
    """Calculates and returns the ratios of consecutive Fibonacci numbers up to a limit."""
    a, b = 0, 1
    ratios = []
    for _ in range(2, limit + 1):
        ratio = b / a if a != 0 else None 
        if ratio is not None:
            ratios.append(ratio)
        a, b = b, a + b
    return ratios

limit = 10
ratios = fibonacci_ratios(limit)
print(f"Ratios of consecutive Fibonacci numbers up to F({limit}): {ratios}")
