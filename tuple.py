odd_numbers = (1, 3, 5, 7, 9, 11,3, 13, 15, 17, 19,11,13,21,23,15,25,27,29,31,33,35,37,39)
#odd_numbers[0] = 2 # This will raise a TypeError because tuples are immutable

#we can also create a tuple using the tuple() constructor
even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
tuple_even_numbers = tuple(even_numbers)
print(tuple_even_numbers)

#to check if an element is in a tuple
print(5 in odd_numbers) # True
print(6 in odd_numbers) # False

#to unpack a tuple into variables
first, second, third, *rest = odd_numbers
print(first) # 1
print(second) # 3
print(third) # 5
print(rest) # (7, 9, 11, 13, 15, 17, 19)

# we can slice a tuple just like a list
print(odd_numbers[0:5]) # (1, 3, 5, 7, 9)
print(odd_numbers[-5:]) # (11, 13, 15, 17, 19)

#if we want to delete or remove an element we can't do that because tuples are immutable, and we will get an error
del odd_numbers[0] # This will raise a TypeError because tuples are immutable

#but if we want to delete an item we can convert the tuple to a list, delete the item, and then convert it back to a tuple
temp_list = list(odd_numbers)   
temp_list.remove(1) # remove the first element
odd_numbers = tuple(temp_list) # convert back to a tuple
print(odd_numbers) # (3, 5, 7, 9, 11, 13, 15, 17, 19)

#to check the length of a tuple
print(len(odd_numbers)) # 9

#to determine the index of an element in a tuple
print(odd_numbers.index(9)) # 3

#to determine the index of an element with starting position
print(odd_numbers.index(9,6,13))
#to count the number of occurrences of an element in a tuple
print(odd_numbers.count(3)) # 1
print(odd_numbers.count(2)) # 0

#to sort a tuple
sorted(odd_numbers)
print(odd_numbers)

#to reverse a tuple using sorted() method
sorted(even_numbers, reverse=True)
print(even_numbers)