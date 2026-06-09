celsuis = [25, 45, 30, 15, 10]
# Using map to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
fahrenheit = list(map(celsius_to_fahrenheit, celsuis))
print(fahrenheit)


numbers = list(range(1, 100))
# Using filter to get even numbers from the list
def is_even(number):
    return number % 2 == 0
even_numbers = list(filter(is_even, numbers))
print(even_numbers)


