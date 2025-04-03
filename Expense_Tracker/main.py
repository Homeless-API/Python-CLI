from pathlib import Path
from tabulate import tabulate
import datetime
import os
import json

current_path = Path(__file__)
parent_path = current_path.parent



def write_data(data):
    data_path = os.path.join(parent_path, 'expense_db.json')

    try:
        with open(data_path, 'r') as file:
            data_fetched = json.load(file)
            if not isinstance(data_fetched, list):  # Ensure it's a list
                data_fetched = []
    except:
        data_fetched = []
    
    # Append the single dictionary, not a list
    data_fetched.append(data)

    with open(data_path, 'w') as file:
        json.dump(data_fetched, file, indent=4)

    

def read_data():
    data_path = os.path.join(parent_path, 'expense_db.json')

    try:
        with open(data_path, 'r') as file:
            return json.load(file)
    except:
        return []

def id():
    data = read_data()
    if data:
        return data[-1]['id'] + 1
    else:
        return 1
    

def add_expenses():


    expense_name = input("Enter expense name: ")
    expense_amount = input("Enter expense amount: ")
    date = datetime.datetime.now()
    expense_date = date.strftime("%Y-%m-%d")
    
    data = {'id': id(), 'name': expense_name, 'amount': expense_amount, 'data_entered': expense_date}

    write_data(data)

def list_expense():
    data = read_data()
    if data:
        table_data = [[expense['id'], expense['name'], expense['amount'], expense['data_entered']] for expense in data]
        
        # Define table headers
        headers = ['id', "Expense Name", "Amount", "Date"]
        
        # Generate and print the table
        table = tabulate(table_data, headers=headers, tablefmt="grid")
        print(table)
    else:
        print("No expenses recorded.")

def monthly_expense(month):
    data = read_data()
    if data:
        for expense in data:
            expense_date = expense['data_entered']
            expense_month = expense_date.split('-')[1]
            print(expense_month)
            if expense_month == month:
                print(f"ID: {expense['id']}, Expense: {expense['name']}, Amount: {expense['amount']}, Date: {expense['data_entered']}")
            else:
                print("month not found or not in zero-padded format")

def total_amount():
    data = read_data()
    amounts = []
    if data:
        for expense in data:
            expense_amount = expense['amount']
            amounts.append(float(expense_amount))
        
        print(f"Your total expenditure this month is: {sum(amounts)}")

def delete_expense(given_id):
    data = read_data()
    data_path = os.path.join(parent_path, 'expense_db.json')
    given_id = int(given_id)  # Ensure the given ID is an integer
    
    if data:
        # Filter out the expense with the matching ID
        updated_data = [expense for expense in data if expense['id'] != given_id]
        
        # Check if the size of data changed (indicating a deletion)
        if len(updated_data) < len(data):
            with open(data_path, 'w')as f:
                json.dump(updated_data, f, indent=4)
            print("Expense deleted successfully.")
        else:
            print("Expense not found.")
    else:
        print("No expenses recorded.")


while True:
    command = input("***")
    if command == "add expense":
        add_expenses()
    elif command == "list expense":
        list_expense()
    elif command == f"list expense - m":
        month = input("input the month in zero-padded format: ")
        monthly_expense(month)
        pass
    elif command == "expense tracker summary":
        total_amount()
    elif command == 'delete expense':
        given_id = input('Give the id of the expense to be deleted: ')
        delete_expense(given_id)
    elif command == "quit" or command == "exit":
        break
    else:
        print("Unrecodgnized Command, try again!!")
