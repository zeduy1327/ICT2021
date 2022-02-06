import random
import string

students = [None]*300
scores = [None]*300

index = 0
for student in students:
    # printing lowercase
    letters = string.ascii_lowercase
    studentname = ''.join(random.choice(letters) for i in range(5))
    studentnumber = random.randint(100, 999)
    students[index] = studentname + str(studentnumber)
    scores[index] = random.randint(0, 10)
    index+=1

index = 0
for student in students:
    print(students[index] + ": " + str(scores[index]))
    index += 1