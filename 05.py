'''
# --------------------------------------- #
#          5: PIN CHECKER + ATM           #
# --------------------------------------- #

In this portion of the assignment, you'll be using "functions". A function is just
a reusable block of code. Don't worry too much about these for now!

Normally when you write a function, you need to write a docstring to go with it. 
For this assignment, we've written them for you, but you'll have to write them yourself 
in the future!

------------------
   INTRODUCTION
------------------

You have just been hired by Budget Bank to create a program for their ATM machine.
Budget Bank isn't very security conscious, so the only thing a user needs to enter to
access their account is a PIN number. A valid PIN number must:
  - Be exactly 4 digits long
  - Have those 4 digits add up to 10 or more (>=10)

Once a user has entered a valid PIN and entered their account, they can check their
balance, deposit money, withdraw money, enter a lottery to gain or lose money, or quit
the program.

Now get out there and implement some bare minimum security!

--------------
   OBJECTIVE
--------------

You will build a simple ATM program that:
  1. Asks the user for a 4 digit PIN and checks if it’s valid.
  2. If the PIN is valid, allows the user to interact with an ATM menu.
  3. The ATM menu allows the user to check balance, deposit, withdraw, enter a lottery, or quit.

-----------------------
   ATM FUNCTIONALITY
-----------------------

Your ATM program should start by prompting the user to enter a 4 digit PIN and checking if it
is valid. You do NOT have to worry about the user entering a value that is not a positive number.

One the user has entered a valid PIN (4 digits and it adds up to 10 or more),
the ATM should display a menu that allows the user to select from the following options:

CHECK BALANCE:
  - Output the amount of money the user has in their account
  - The balance should start at 0
  Sample input:
    check balance
  Sample Output:
    Balance: $100

DEPOSIT:
  - Asks the user how much money they want to deposit
  - If the user enters a negative number, output an error message.
  - If the user enters a positive number, add it to the balance in the account.
  - Display how much was deposited
  Sample input:
    deposit
    100
  Sample Output:
    Balance: $100

WITHDRAW:
  - Asks the user how much money they want to withdraw
  - If the amount is negative or more than the current balance, print an error message
  - If the amount is positive and less than the current balance, subtract it from the balance in the account
  - Display how much was withdrawn
  Sample input:
    withdraw
    500
  Sample Output:
    Balance: $200

LOTTERY:
  - Adds or removes a random amount of money from the user's account.
  - The amount should be within the range of -$500 and $500.
  - Display how much was won/lost, then update and print the new balance.
  - Account balance can go negative. For example, if user had $10 and lost $20 their new balance is -$10.
  Sample input:
    lottery
  Sample Output:
    You won $50 and your new balance is $150!

QUIT:
  - This case is handled by the loop. Don't worry about implementing it, though you should be aware of it
    when writing the "invalid option" case.
  - When quitting, also display the final balance in the user's account. 
  Sample input:
    quit
  Sample Output:
    Your final balance is: $500

INVALID OPTIONS:
  - If the user inputs anything else other than these five options (an invalid option),
    output an error message.
  - Do not exit the program. You should just be letting the user know they entered an invalid option
    and prompting for new input.

EXTRA CREDIT:
After the user selects the quit option, print out a "receipt" with every option the user selected and
their balance after each option. This receipt should be printed to a file called "receipt.txt".
  - Example of what this could look like:
    Option: deposit $100 | Balance: $100
    Option: withdraw $50 | Balance: $50
    Option: quit | Balance: $50
'''



import random # Used to generate random numbers for lottery

# -------------------------------------------------------------------------------
# This block of code before 'def pin_checker()' is called a function.
# We will learn more about how these work later!
#
# For now, just focus on writing the logic inside it.
#
# Instead of printing in our if/else blocks like in Problem 4,
# we will be 'returning', specifically, adding the line:
#     return True   (If the PIN is valid)
#     return False  (If the PIN is NOT valid)
#
# Think of this as sending back a YES or a NO answer
# You do NOT need to print anything, just "return" the result.
#
# This function will check if the user's PIN is valid
# A PIN is valid if it has 4 digits and they sum up to 10 or more
# You do not have to handle input that is not a positive number
# PINs that start with 0 can be valid, e.g. 0345 is valid.
# -------------------------------------------------------------------------------
def pin_checker():
  """
    Prompts the user to enter a 4-digit PIN and evaluates whether it is valid.

    A PIN is valid if:
      - It contains exactly 4 digits.
      - The sum of the digits is 10 or greater.

    The function does not handle non-numeric input, under the assumption that the
    user enters a positive integer.

    Returns:
        bool: True if the PIN is valid, False otherwise.
  """
  # Prompt the user to enter a PIN and check whether it is valid
  # Hint: The division (/) and modulo (%) functions will be very helpful here.
  # You can also do problem with string manipulation but we haven't covered that yet!
  # Sample input:
  # 12345 (returns False)
  # 1111 (returns False)
  # 5678 (returns True)
  ### CODE GOES HERE ###




# Don't worry about how functions works yet, just follow the comments below!
def main():
  """
    Controls the flow of the ATM program.

    This function:
      - Repeatedly asks the user for their PIN until it is valid.
      - Displays the ATM menu once authenticated.
      - Allows the user to:
            - Check their balance
            - Deposit money
            - Withdraw money
            - Enter a lottery (gain or lose money)
            - Quit the program
      - Maintains and updates the user's account balance.

    No value is returned - the program runs until the user selects "Quit".
  """
  print("-------- Problem 5 --------")
  valid_pin = False # This keeps track of whether the user has entered a valid PIN or not


  # NEW CONCEPT: WHILE LOOP
  #
  # This is a while loop, don't worry too much about how it works yet, but
  # essentially, It will keep repeating a block of code until something changes
  #
  # In our case:
  #    - The first loop keeps asking for a PIN until the user enters a valid one
  #    - The second loop will keep running until the user types "quit"
  while (not valid_pin):
      valid_pin = pin_checker()

  # At this point pf the code, the user has entered a valid PIN

  # This variable will store menu choice that the user has chose
  # You'll use this variable to check what action they want to take
  # Feel free to add any other variables, you may need to create another one
  user_input = ""


  while (user_input != "quit"): # Loops until the user chooses to quit
      # Accepts user input and converts to lowercase
      user_input = input("Select an option: Check Balance, Deposit, Withdraw, Lottery, or Quit: ").lower()


      # Implement the ATM menu here
      # Remember that you DO NOT have to implement the "Quit" option
      # BUT you DO have to implement an "invalid option" case that catches invalid options
      # And "Quit" is a VALID option
      ### CODE GOES HERE ###


  # Print the user balance here
  ### CODE GOES HERE ###



  # Extra credit should also go here if you choose to do it!
  # You can also implement your extra credit in the while loop if you would like!
  ### CODE GOES HERE ###


# This is where you program will start and tells python to run your program!
if __name__ == "__main__":
    main() # The program will run by running the main function


