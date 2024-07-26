import pandas as pd
from tabulate import tabulate

def start():

    """ 
    The function expalin how the program it's working and for what it is.
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
    
    """ 
    The function calculate the sum to be always float, if it's a string it'll be 
    displayed error, if it's less then 4 digits it will print again error message
    """

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

    """ 
    The def calculate the month income in % for needs, savings
    and living
    """

    needs = 0.4 * income
    savings = 0.4 * income
    living = 0.2 * income
    return needs, savings, living

def add_new_needs(needs_row):

    """ 
    The def first will ask the user to aadd a new row or not.
    if the asnwer is yes it will be asked to add new name and sum.
    If statement to mamke the user to use only alphabetical characters.
    """

    while True:   
        add_new_row = input("Do you want to add a new row for 'Needs'? (yes/no): ")
        if add_new_row == 'yes':
            try:
                new_name = input("Enter new name for Needs: ") 
                if not new_name.isalpha():
                    print("Please enter only alphabetical characters for name.")
                    return add_new_needs(needs_row)
                new_sum = float(input("Enter new value: "))
                new_row = [f"{new_name}", f"${new_sum}", "-", "-", "-", "-"]
                needs_row.append(new_row)
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        else:
            break
            #main_menu()

def add_new_savings(savings_row):

    """ 
    The def first will ask the user to add a new row or not.
    if the answer is yes it will be asked to add new name and sum.
    If statement to mamke the user to use only alphabetical characters.
    """

    while True:   
        add_new_row = input("Do you want to add a new row for 'Savings'? (yes/no): ")
        if add_new_row == 'yes':
            try:
                new_name = input("Enter new name for Savings: ") 
                if not new_name.isalpha():
                    print("Please enter only alphabetical characters for name.")
                    return add_new_savings(savings_row)
                new_sum = float(input("Enter new value: "))
                new_row = ["-", "-", f"{new_name}", f"${new_sum}", "-", "-"]
                savings_row.append(new_row)
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        else:
            break
            #main_menu()
            
def build_table(needs, savings, living, choice):

    """ 
    The def add the data from def calculate_and_input_expense() and make
    it in a table.
     """

    table = ["Name", "Needs", "Name", "Savings/Investments","Name", "Living Expenses"]
    info_income = [[f"{"-"}", f"${needs}", f"{"-"}", f"${savings}", f"{"-"}", f"${living}"]]
    if choice == 1:
        add_new_needs(info_income)
    elif choice == 2:
        add_new_savings(info_income)
    print(tabulate(info_income, headers=table, tablefmt="simple"))

def main_menu():

    """ Runs the navigation menu. Give a choice to the user to choose 
    from 4 different options. When the user make a choise it will be send
    to the proper function.
    """
    
    while True:
        print()
        print("Please select one of the following options:\n")
        print()
        print("1. Add Needs:")
        print("2. Add Savings:")
        print("3. Add Living expences:")
        print("4. Stop additing and see the result:")

        try:
            user_input = input("- ")
            if user_input in ["1", "2", "3", "4"]:
                choice = int(user_input)
                build_table(needs, savings, living, choice)
                break
            else:
                raise ValueError("")
        except ValueError as e:
            print()
            print("Invalid input: Please select one of the options (1-4).\n")
     
#start()
income = get_income()
needs, savings, living = calculate_and_input_expense(income)
main_menu()

