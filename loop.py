class_first_students = ["Alice", "Bob", "Charlie", "David", "Eve"]
# Looping through the list of students
for student in class_first_students:
    print(student)

#to nest a loop inside another loop
students_rankings = [1, 2, 3, 4, 5]
for student in class_first_students:
    for ranking in students_rankings:
        print(f"{student} is  {ranking} in the class")

#while loop with a short game example
number_to_guess = 7
guess = None
while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 10:"))
    if guess != number_to_guess:
        print("Wrong guess, try again!")
    else:
        print("Congratulations! You guessed the number.")