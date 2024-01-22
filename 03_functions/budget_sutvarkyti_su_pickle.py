""" Komandinio darbo / savarankiška užduotis
===[ Biudžetas ]===

Reikalavimai

* Biudžeto turinys - pajamų/išlaidų žurnalo žodynas
** raktas - paskirtis
** reikšmė - pajamos pozityvus float, išlaidos negatyvus float
* Galimybė pridėti pajamas arba išlaidas
* Spausdinti pajamų/išlaidų žurnalą
* Suskaičiuoti biudžeto balansą

"""

import os 
import pickle

BUDGET_FILE = 'budget.pickle'

if os.path.exists(BUDGET_FILE):
    with open(BUDGET_FILE, 'rb') as file:
        transactions = pickle.load(file) #cia susitvarkyti pagal save
else:
    transactions = {}

def add_income(income, amount, income_type):
    income += amount
    print(f"Income added: {amount} ({income_type})")
    return income

def add_expense(expenses, amount, expense_type):
    expenses += amount
    print(f"Expense added: {amount} ({expense_type})")
    return expenses

def calculate_balance(income, expenses):
    balance = income - expenses
    print(f"Current balance: {balance}")

income = 0
expenses = 0
income_types = []
expense_types = []

while True:
    print("\nOptions:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Calculate Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter the income amount: "))
        income_type = input("Enter the type of income: ")
        income_types.append(income_type)
        income = add_income(income, amount, income_type)
    elif choice == '2':
        amount = float(input("Enter the expense amount: "))
        expense_type = input("Enter the type of expense: ")
        expense_types.append(expense_type)
        expenses = add_expense(expenses, amount, expense_type)
    elif choice == '3':
        calculate_balance(income, expenses)
        print("\nIncome Types:", income_types, income)
        print("Expense Types:", expense_types, expenses)
    elif choice == '4':
        with open(BUDGET_FILE, 'wb') as file:
            pickle.dump(transactions, file)
        print("Exiting the budget calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
