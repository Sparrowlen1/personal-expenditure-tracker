import json
from datetime import datetime

expenses = [] #we are declaring this as a local variable
def add_expense():
    name = input("Name of the item? ")
    description = input("whats the description name? ")
    amount = float(input("What is the price for this product? "))
    date =input("enter the date(YYYY-MM-DD)? ")

    expense = {"NAME":name, "DESCRIPTION":description, "AMOUNT":amount, "DATE":date}

    expenses.append(expense)
    print("expenses added successfully")


def view_expenses():
    for expense in expenses:
        print(f"{expense['NAME']}: {expense['DESCRIPTION']} - {expense['DATE']} - {expense['AMOUNT']}") #We are retrieving the items in the variable named expense


def calculate_total():
    total = sum(expense["AMOUNT"] for expense in expenses)          
    print(f' the total expense is: {total}')


#applying json to save and load the data retrieved from our user
#saving the data

def save_data(filename='expenses.json'):
    with open(filename,'w') as file: #fike handling
        json.dump(expenses,file) #This line uses json.dump to convert the expenses list (a Python data structure) into JSON format and writes it to the file.
    print("our file has been saved successfully") 

 # now loading the data

def load_data(filename='expenses.json'):
    global expenses #since we havent defined the variable hence its a global variable
    try:
        with open(filename,'r') as file: #file handling
            expenses = json.load(file) #Uses json.load to read the JSON data from the file and converts it back into a Python data structure
    except FileNotFoundError: 
        print("no previous data found")      

def main():
    load_data() #now we are loading the data that we have read
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Save and Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            save_data()
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()