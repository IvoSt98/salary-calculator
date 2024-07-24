import pandas as pd
from tabulate import tabulate

def start():
    """ the function expalin how the program it's working and for what it is.
    """
   
    print("Welcome to Your Salary/Income Calculator!\n")
    print("The 40/40/20 System:\n")
    print("First, enter your income, which will be divided as follows:")
    print("40 percentages - needs, 40 percentages - savings/investments, and 20 percentages - living expenses.")
    print("Next, add your expenses by selecting a category and entering the purpose and amount. ")
    print("In the end, you'll know if you're managing your finances well.\n")
    print("Good Luck!/n")
    print("Press enter to start")
    
start()

def get_income():

    """ The function calculate the sum to be always float, if it's a string it'll be 
    displayed error, if it's less then 4 digits it will print again error message"""

    while True: 
        try:
            user_income = input("Enter your income (at least 4 digits): ")
            income = float(user_income)
            if income >= 1000:  
                return income
            else:
                print("Income must be at least 4 digits. Please try again.")
        except ValueError:
            print("Invalid data. Please enter a number with at least 4 digits.")
            
get_income()



