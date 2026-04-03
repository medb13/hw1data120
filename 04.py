'''
# --------------------------------------------------------- #
#    4: CONDITIONAL STATEMENTS, RANDOM NUMBER GENERATION    #
# --------------------------------------------------------- #

Slides to reference: 1.2 Python Basics & 1.3 Control Flow

In this part, you will practice with
     - 'Conditional statements', allows our program to make decisions
     - 'random' module, used to generate a random number within a range and
        are useful for testing code.
'''

print("-------- Problem 4 --------")

# Random number generators need the random module
# We will be covering modules more in the future so don't worry about this line for now!
import random

# -----------------------------------
#      Part 1: Pass Fail Checker
# -----------------------------------

# Step 1: Prompt the user to enter their numeric grade (0 - 100)
#         The input will be a number, do not worry about invalid input (e.g. a boolean)
#         Make sure to check if the number is in that range!
#         If the number is not in range, tell the user it was invalid then set their grade to zero.
# Step 2: Use Conditional statements to determine
#         - Their letter grade (A, B, C, D, and F)
#             - An A is greater or equal to a 90, a B is greater than or equal to 80, and so on.
#         - Whether or not they are passing (C and above) or failing (D and below)
# Step 3: Print their grade and whether they are passing or failing
#         e.g. Input: 87 | Output: "You have a[n] B and you are passing"
#              Input: 67 | Output: "You have a[n] D and you are failing"
### CODE GOES HERE ###


# -----------------------------------
#      Part 2: Applying a Curve!
# -----------------------------------

# The professor has decided to curve the class! Hooray!

# Step 1: Generate a random number between 1 and 20
# Step 2: Add this value to the user's grade from Part 1.
# Step 3: Output the curve, their new letter grade, and whether they are failing.
#         Grades above 100 are valid, and the user has an A if that happens.
#         e.g. Input: 87 | Output: "With a curve of 5, you have a[n] A and you are passing"
#              Input: 67 | Output: "With a curve of 2, you have a[n] D and you are failing"
### CODE GOES HERE ###

