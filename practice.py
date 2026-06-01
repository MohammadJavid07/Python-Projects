"""fruits = ["apple", "banana", "orange", "grape", "kiwi", "melon", "peach", "pear", "plum", "strawberry"]
# 1. Print the first three fruits in the list.
print(fruits[0:3]) 
# 2. Print the last two fruits in the list.
print(fruits[-1:-3:-1])
fruits[3] = "cherry"
print(fruits)
del fruits[2]
print(fruits)"""

employee = ["John", 34, "Web Developer", 50000, "john@example.com"]
#update the employee's job title and salary
name,age,*rest= employee

#to print the length of the employee list
print(len(employee))
#to add a new element to the employee list
employee.append("Jalalabad-Afghanistan")
#to nest a list inside another list
technologies = ["Python", "JavaScript", "HTML", "CSS"]
employee.append(technologies)
print(employee[5])
#to extend a list with another list
moreTechnologies = ["Django", "React"]
employee.extend(moreTechnologies)
print(employee)
#to remove an element from a list
employee[6].remove("Python")
employee[6].remove("JavaScript")
employee[6].remove("HTML")
employee[6].remove("CSS")
del employee[6]
employee.remove("Django")
employee.remove("React")
print(employee)

#to insert an element at a specific index
employee.insert(2, "Senior Web Developer")
print(employee)