'''
# --------------------------------------- #
#      2: Data Types Assignment           #
# --------------------------------------- #

Slides to reference: 1.2 Week1-Python Basics

For this section
     - Please follow the directions carefully
     - After each prompt, finish the given line of code

'''
print("-------- Problem 2 --------")


# In Python, we use different data types to represent different kinds of information.
# Below are some of the most common data types you'll use:

# ----------------------------
#        INTEGER (int)
# ----------------------------
# Integers represent positive and negative whole numbers.
# We use them when we need to count or do math with whole numbers.
# Example: age, number of siblings, etc.

# Your turn!
my_age =   # add your age

# ----------------------------
#        FLOAT (float)
# ----------------------------
# Floats are numbers with decimal points.
# We use them when precision is important, like measurements.
# Example: height, weight, temperature, etc.

# Your turn!
my_height =   # add your height

# ----------------------------
#         STRING (str)
# ----------------------------
# Strings are used for text. Anything inside quotes is a string.
# Example: your name, address, favorite color, etc.

# Your turn!
my_name =   # add your name

# ----------------------------
#        BOOLEAN (bool)
# ----------------------------
# Booleans are either True or False.
# We use them for yes/no, on/off, true/false situations.
# Example: is the light on? are you a student?

# Your turn!
is_student =   # add your status

# ----------------------------
#          CONSTANTS
# ----------------------------
# Constants are variables that should not change once set.
# In Python, we write them in all caps by convention.
# Example: the temperature water boils

# Your turn!
WATER_BOILING_POINT_F = # add the temperature that water boils in Fahrenheit

# ----------------------------
#        TYPE CONVERSION
# ----------------------------
# input() ALWAYS returns a string, even if the user types a number.
# Convert the values below into the correct numeric types.

# Your turn!
age_input = input("Enter your age: ")       # this is a string
# Convert age_input into an integer and store it in age_as_int
### CODE GOES HERE ###

height_input = input("Enter your height in feet (example: 5.9): ")  # also a string
# Convert height_input into a float and store it in height_as_float
### CODE GOES HERE ###


# ----------------------------
#          PRINTING
# ----------------------------

print("my name is:", my_name)
print("I'm", my_age, "years old.")
print("My height is", my_height, "feet.")
print("Am I a student at the University of Maryland?", is_student)
print("Water boils at", WATER_BOILING_POINT_F, "degrees Fahrenheit.")
