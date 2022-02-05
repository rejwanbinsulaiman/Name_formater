
def formate_name(f_name, L_name):
"""
This function takes Two inputs and Print them in a formated manner 
"""

  fname = f_name.title() 
  lname = L_name.title()
  print(f"{fname} {lname}")

formate_name(input("Enter your First name: "), input("Enter your last name: "))