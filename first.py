print("Hello world!")
my_range = range(10)
print(my_range)
for i in my_range:{
    print(i)
}
my_list = ["Javid","Ali", "Huseyn","Muzafar","Khanwali"]
print(my_list)

# this is a comment
day = "Today's day is Monday"
print(day)
print(len(day))
weather = "The weather is sunny"
#string concatenation
dayAndWeather = day + " " +"and "+ weather
print(dayAndWeather)

#concatenation string with numbers
number = 10
numberString = "The number is "
# this will cause an error because we cannot concatenate a string with a number
# numberAndString = numberString + number   
# to fix this we can convert the number to a string
numberAndString = numberString + str(number)
print(numberAndString)

#f-strings
name = "Javid"
age = 25    
greeting = f"My name is {name} and I am {age} years old."
print(greeting)
#string slicing
fullName = "mohammad javid miakhil"
print(fullName[0]) # m
print(fullName[1:4]) # oha
print(fullName[:8]) # mohammad
print(fullName[9:]) # javid miakhil
print(fullName[9:14]) # javid               
print(fullName[15:20]) #  Miakhil       
print(fullName[0:21:2]) # Mhma ai iki   
#to reverse a string using slicing
print(fullName[::-1]) # lihkaiM divaJ dammahoM  
#string methods 
#to convert a string to uppercase
print(fullName.upper()) # MOHAMMAD JAVID MIAKHIL
#to convert a string to lowercase
print(fullName.lower()) # mohammad javid miakhil
#to replace a substring with another substring
print(fullName.replace("Javid", "Ali")) # Mohammad Ali Miakhil
#to split a string into a list of substrings        
print(fullName.split()) # ['Mohammad', 'Javid', 'Miakhil']
#to join a list of strings into a single string
nameList = ["Mohammad", "Javid", "Miakhil"]
print(" ".join(nameList)) # Mohammad Javid Miakhil
#to check if a string starts with a certain substring   
print(fullName.startswith("Mohammad")) # True
#to check if a string ends with a certain substring
print(fullName.endswith("Miakhil")) # True  
# striping whitespace from a string
whitespaceString = "   Hello world!   "
print(whitespaceString.strip()) # Hello world!  
#to find the index of a substring in a string
print(fullName.find("Javid")) # 9
#to capitalize the first letter of a string
print(fullName.capitalize()) # Mohammad javid miakhil
#to count the number of occurrences of a substring in a string
print(fullName.count("a")) # 3
#to check if a string is a digit
numberString = "12345"
print(numberString.isdigit()) # True
#to check if a string is alphabetic
alphaString = "Hello"   
print(alphaString.isalpha()) # True
#to check if a string is alphanumeric
alphanumericString = "Hello123"
print(alphanumericString.isalnum()) # True
#to check if a string is a valid identifier
identifierString = "my_variable"
print(identifierString.isidentifier()) # True
#to check if a string is a valid email address
emailString = "user@example.com"
print(emailString.find("@") != -1 and emailString.find(".") != -1) # True
#to check if a string is a valid URL
urlString = "https://www.example.com"
print(urlString.startswith("https://")) # True
#to check if a string is a lowercase string
lowercaseString = "hello world"
print(lowercaseString.islower()) # True
#to check if a string is an uppercase string
uppercaseString = "HELLO WORLD" 
print(uppercaseString.isupper()) # True
#to make a string title case
print(fullName.title()) # Mohammad Javid Miakhil

# to calculate the total bill for a group of friends at a restaurant
running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill,2)
print(f'Each person pays: {each_pays}')

#Movie ticket booking calculator
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    final_price = base_price - discount + extra_charges +service_charges
    print('Final price of ticket:',final_price)  
else:
    print('Ticket booking failed due to restrictions')