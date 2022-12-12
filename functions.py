def factorial(number):
    if isinstance(number, int):
        result = 1
        for num in range(2, number + 1):
            result *= num
        return result


def fibonacci(number):
    if number == 1:
        return [1]
    if number == 2:
        return [1, 1]
    fibonacci_numbers = [1, 1]
    for _ in range(2, number):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers
