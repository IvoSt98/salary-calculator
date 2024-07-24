import pandas as pd
from tabulate import tabulate

def start():

    """ The function expalin how the program it's working and for what it is.
    """
   
    print("     Welcome to Your Salary/Income Calculator!\n     ")
    print("     The 40/40/20 System:\n      ")
    print(" First, enter your income for a month, which will be divided as follows: ")
    print(" 40 percentages - needs, 40 percentages - savings/investments, and 20 percentages - living expenses.\n   ")
    print("-Example for NEEDS: this is your insuarance for the car, bills, credits, food and etc. The things without you can't live. ")
    print("-Example for SAVINGS/INVESTMENTS: this is where you will write the money for education, for your holiday, investments in stocks and etc.")
    print("-Example for LIVING EXPENSES: here you need to fill your money for cigaretes, parties, restaurants and etc. Something without you can survive\n")
    print(" Next, add your expenses by selecting a category and entering the purpose and amount. ")
    print(" In the end, you'll know if you're managing your finances well.\n ")
    print("     Good Luck!\n        ")
    

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
     
def calculate_and_input_expense(income):

    """ The def calculate the month income in % for needs, savings
    and living"""

    needs = 0.4 * income
    savings = 0.4 * income
    living = 0.2 * income
    return needs, savings, living

def build_table(needs, savings, living):

    """ The def add the data from def calculate_and_input_expense() and make
    it in a table. """
    
    table = ["Needs", "Savings/Investments", "Living Expenses"]
    info_income = [[f"${needs}", f"${savings}", f"${living}"]]
    print(tabulate(info_income, headers=table, tablefmt="simple"))

start()
income = get_income()
needs, savings, living = calculate_and_input_expense(income)
build_table(needs, savings, living)

