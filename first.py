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
