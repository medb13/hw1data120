'''
# --------------------------------------- #
#          5: PIN CHECKER + ATM           #
# --------------------------------------- #
'''

import random # Used to generate random numbers for lottery

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
  pin = int(input("Enter your 4-digit PIN: "))

  if pin < 0 or pin > 9999:
      return False

  d1 = pin // 1000
  d2 = (pin // 100) % 10
  d3 = (pin // 10) % 10
  d4 = pin % 10

  if d1 + d2 + d3 + d4 >= 10:
      return True
  else:
      return False




# Don't worry about how functions works yet, just follow the comments below!
def main():
  """
    Controls the flow of the ATM program.
  """
  print("-------- Problem 5 --------")
  valid_pin = False # This keeps track of whether the user has entered a valid PIN or not

  while (not valid_pin):
      valid_pin = pin_checker()

  user_input = ""
  balance = 0


  while (user_input != "quit"): # Loops until the user chooses to quit
      user_input = input("Select an option: Check Balance, Deposit, Withdraw, Lottery, or Quit: ").lower()

      if user_input == "check balance":
          print("Balance: $" + str(balance))

      elif user_input == "deposit":
          amt = int(input("Enter amount: "))
          if amt < 0:
              print("Invalid amount.")
          else:
              balance += amt
              print("Balance: $" + str(balance))

      elif user_input == "withdraw":
          amt = int(input("Enter amount: "))
          if amt < 0 or amt > balance:
              print("Invalid amount.")
          else:
              balance -= amt
              print("Balance: $" + str(balance))

      elif user_input == "lottery":
          change = random.randint(-500, 500)
          balance += change
          if change >= 0:
              print("You won $" + str(change) + " and your new balance is $" + str(balance) + "!")
          else:
              print("You lost $" + str(abs(change)) + " and your new balance is $" + str(balance) + "!")

      elif user_input != "quit":
          print("Invalid option.")


  # Print the user balance here
  print("Your final balance is: $" + str(balance))



  # Extra credit should also go here if you choose to do it!
  # You can also implement your extra credit in the while loop if you would like!
  ### CODE GOES HERE ###


# This is where you program will start and tells python to run your program!
if __name__ == "__main__":
    main() # The program will run by running the main function
