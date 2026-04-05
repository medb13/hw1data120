'''
# --------------------------------------- #
#            3: Operators!                #
# --------------------------------------- #
'''

print("-------- Problem 3 --------")

# -----------------------------------
#    Part 1: Assignment Operators
# -----------------------------------

x = 20

# 1. Add 5 to x
x += 5

# 2. Subtract 3 from x
x -= 3

# 3. Multiply x by 2
x *= 2

# 4. Divide x by 4
x /= 4

# 5. Use floor division on x with 2
x //= 2

# 6. Get the remainder of x when divided by 3
x %= 3

# 7. Raise x to the power of 2
x **= 2

# Print the final value of x
print("the final value of x:", x)

# -----------------------------------
#    Part 2: Membership Operators
# -----------------------------------

text = "Wow, Python is so cool!"

# 1. Check if "p" is in the string
print("Is 'p' in text?", "p" in text)

# 2. Check if "z" is not in the string
print("Is 'z' not in text?", "z" not in text)

# 3. Check if space is in the string
print("Is space in text?", " " in text)

# 4. Check if "Python" is in the string
print("Is 'Python' in text?", "Python" in text)

# -----------------------------------
#     Part 3: Identity Operators
# -----------------------------------

a = [1, 2, 3]
b = [1, 2, 3]
c = a

# 1. Check if a and b are the same object
print("a is b:", a is b)

# 2. Check if a and b have the same content
print("a == b:", a == b)

# 3. Check if a and c are the same object
print("a is c:", a is c)

# 4. Check if b and c are NOT the same object
print("b is not c:", b is not c)
