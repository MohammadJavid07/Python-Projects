numbers = list(range(1, 100))
# filtering just odd numbers using a function
def is_odd(num):
    return num % 2 != 0
odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))
