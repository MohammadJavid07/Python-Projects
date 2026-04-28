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
