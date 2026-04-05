'''
# --------------------------------------------------------- #
#    4: CONDITIONAL STATEMENTS, RANDOM NUMBER GENERATION    #
# --------------------------------------------------------- #
'''

print("-------- Problem 4 --------")

import random

# -----------------------------------
#      Part 1: Pass Fail Checker
# -----------------------------------

grade = int(input("Enter your grade (0-100): "))

if grade < 0 or grade > 100:
    print("Invalid grade entered")
    grade = 0
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"
if grade >= 70:
    status = "passing"
else:
    status = "failing"

print("You have a[n]", letter, "and you are", status)

# -----------------------------------
#      Part 2: Applying a Curve!
# -----------------------------------

curve = random.randint(1, 20)
new_grade = grade + curve

if new_grade >= 90:
    new_letter = "A"
elif new_grade >= 80:
    new_letter = "B"
elif new_grade >= 70:
    new_letter = "C"
elif new_grade >= 60:
    new_letter = "D"
else:
    new_letter = "F"

if new_grade >= 70:
    new_status = "passing"
else:
    new_status = "failing"

print("With a curve of", curve, "you have a[n]", new_letter, "and you are", new_status)
