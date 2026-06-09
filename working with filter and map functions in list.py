celsuis = [25, 45, 30, 15, 10]
# Using map to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
fahrenheit = list(map(celsius_to_fahrenheit, celsuis))
print(fahrenheit)


